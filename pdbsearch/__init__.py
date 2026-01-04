import os
import requests
from dataclasses import dataclass
from pdbsearch.terms import TEXT_TERMS, TEXT_CHEM_TERMS
from pdbsearch.schema import update_terms_from_api

if not os.environ.get("PDBSEARCH_NO_UPDATE"):
    update_terms_from_api()

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

@dataclass
class TerminalNode:
    service: str
    parameters: dict

    def serialize(self):
        """Creates the JSON-serializable representation of the node.
        
        :rtype: ``dict``"""

        return {
            "type": "terminal",
            "service": self.service,
            "parameters": self.parameters
        }


def full_text_node(term):
    """Creates a full text node for some search term.
    
    :param str term: the search term.
    :rtype: ``TerminalNode``"""

    return TerminalNode(
        service="full_text", 
        parameters={"value": term}
    )


def text_node(**kwargs):
    """Creates a text node for some search term. Only one key=value pair can be
    provided, and it must correspond to a valid term in the schema.

    :param kwargs: the key=value pairs to create the node from.
    :rtype: ``TerminalNode``"""

    if not kwargs: raise ValueError("At least one keyword argument is required")
    if len(kwargs) > 1: raise ValueError("Only one keyword argument is allowed")
    key, value = next(iter(kwargs.items()))
    parameters = get_text_parameters(key, value)
    return TerminalNode(
        service="text", 
        parameters=parameters
    )


def text_chem_node(**kwargs):
    """Creates a chem_text node for some search term. Only one key=value pair
    can be provided, and it must correspond to a valid term in the schema.

    :param kwargs: the key=value pairs to create the node from.
    :rtype: ``TerminalNode``"""

    if not kwargs: raise ValueError("At least one keyword argument is required")
    if len(kwargs) > 1: raise ValueError("Only one keyword argument is allowed")
    key, value = next(iter(kwargs.items()))
    parameters = get_text_parameters(key, value, text_chem=True)
    return TerminalNode(
        service="text_chem", 
        parameters=parameters
    )


def sequence_node(protein=None, dna=None, rna=None, identity=None, evalue=None):
    """Creates a sequence node, for a protein, DNA, or RNA sequence. One and
    only one of ``protein``, ``dna``, or ``rna`` must be provided.
    
    :param str protein: the protein sequence.
    :param str dna: the DNA sequence.
    :param str rna: the RNA sequence.
    :param float identity: the identity cutoff.
    :param float evalue: the evalue cutoff.
    :rtype: ``TerminalNode``"""

    sequence = protein or dna or rna
    if not sequence: raise ValueError("Sequence not provided")
    if sum(bool(x) for x in [protein, dna, rna]) > 1:
        raise ValueError("Only one sequence type can be provided")
    sequence_type = "protein" if protein else "dna" if dna else "rna"
    parameters = {"sequence_type": sequence_type, "value": sequence}
    if identity is not None: parameters["identity_cutoff"] = identity
    if evalue is not None: parameters["evalue_cutoff"] = evalue
    return TerminalNode(service="sequence", parameters=parameters)


def seqmotif_node(protein=None, dna=None, rna=None, pattern_type="simple"):
    """Creates a seqmotif node for a protein, DNA, or RNA pattern search. One
    and only one of ``protein``, ``dna``, or ``rna`` must be provided.

    :param str protein: the protein pattern.
    :param str dna: the DNA pattern.
    :param str rna: the RNA pattern.
    :param str pattern_type: simple, prosite, or regex.
    :rtype: ``TerminalNode``"""

    pattern = protein or dna or rna
    if not pattern: raise ValueError("Pattern not provided")
    if sum(bool(x) for x in [protein, dna, rna]) > 1:
        raise ValueError("Only one pattern type can be provided")
    sequence_type = "protein" if protein else "dna" if dna else "rna"
    parameters = {
        "value": pattern,
        "pattern_type": pattern_type,
        "sequence_type": sequence_type
    }
    return TerminalNode(service="seqmotif", parameters=parameters)


def structure_node(structure, operator="strict_shape_match"):
    """Creates a structure node for a structure search. You can either provide a
    ``<entry>-<assembly>`` identifier, or a URL to a CIF or BCIF file.
    
    :param str structure: the structure identifier or URL.
    :param str operator: the operator to use for the search.
    :rtype: ``TerminalNode``"""

    value = {}
    if structure.startswith("http"):
        is_bcif = "bcif" in structure
        value = {"url": structure, "format": "bcif" if is_bcif else "cif"}
    else:
        if "-" not in structure:
            raise ValueError("Structure must be in the format of entry-assembly")
        entry_id, assembly_id = structure.split("-")
        value = {"entry_id": entry_id, "assembly_id": assembly_id}
    parameters = {
        "value": value,
        "operator": operator
    }
    return TerminalNode(service="structure", parameters=parameters)


def strucmotif_node(entry, residues, rmsd=None, exchanges=None):
    """Creates a strucmotif node for a structure motif search. You provide a PDB
    ID and a list of residues as tuples of (chain ID, residue number). You can
    also provide residue exchanges, as mappings of (chain ID, residue number) to
    a list of allowed residue names.
    
    :param str entry: the entry ID.
    :param tuple residues: the residues to search for.
    :param float rmsd: the RMSD cutoff.
    :param dict exchanges: the exchanges to search for.
    :rtype: ``TerminalNode``"""

    parameters = {
      "value": {
        "entry_id": entry,
        "residue_ids": [{
            "label_asym_id": residue[0],
            "label_seq_id": residue[1]
        } for residue in residues]
      }
    }
    if rmsd is not None: parameters["rmsd_cutoff"] = rmsd
    if exchanges is not None: parameters["exchanges"] = [{
        "residue_id": {
            "label_asym_id": residue[0],
            "label_seq_id": residue[1]
        },
        "allowed": allowed
    } for residue, allowed in exchanges.items()]
    return TerminalNode(service="strucmotif", parameters=parameters)


def get_text_parameters(key, value, text_chem=False):
    """Generates the parameters dictionary for a text search, using the
    key=value passed to the ``text_node`` function. It will parse the suffixes
    to determine the operator and negation.

    These are the suffixes that produce the corresponding operators (to
    determine whether to use ``equals`` or ``exact_match``, we check the schema
    to see if the term is numeric):

    .. code-block:: text

        __gt                greater_than
        __lt                less_than
        __gte               greater_or_equal
        __lte               less_or_equal
        __in                in
        __exists            exists
        __range             range
        __contains          contains_phrase
        __contains_phrase   contains_phrase
        __contains_words    contains_words
                            equals OR exact_match
    
    :param str key: the key of the term.
    :param value: the value of the term.
    :rtype: ``dict``"""

    terms = TEXT_CHEM_TERMS if text_chem else TEXT_TERMS
    operator, negation = "", False
    lookup = {
        "__gt": "greater_than", "__lt": "less_than",
        "__gte": "greater_or_equal", "__lte": "less_or_equal",
        "__in": "in", "__range": "range",
        "__contains_phrase": "contains_phrase",
        "__contains_words": "contains_words",
        "__contains": "contains_phrase", "__exists": "exists",
    }
    for suffix, key_operator in lookup.items():
        if key.endswith(suffix):
            operator = key_operator
            key = key[:-len(suffix)]
            if suffix == "__range":
                value = {
                    "from": value[0], "to": value[1],
                    "include_lower": isinstance(value, list),
                    "include_upper": isinstance(value, list),
                }
            if suffix == "__exists": negation = False if value else True
            break
    if key.endswith("__not"):
        negation = not negation
        key = key[:-5]
    key = key.replace("__", ".")
    if key not in terms: raise ValueError(f"Invalid term: {key}")
    if not operator:
        is_numeric = "default-match" in terms[key]
        operator = "equals" if is_numeric else "exact_match"
    parameters = {"attribute": key, "operator": operator}
    if operator != "exists": parameters["value"] = value
    if negation: parameters["negation"] = True
    return parameters


def search(return_type, node=None, return_all=False, start=None, rows=None):
    """Queries the RCSB search API.

    :param str return_type: the type of data to return.
    :param bool return_all: whether to return all results, unpaginated.
    :rtype: ``dict``"""

    query = {
        "return_type": return_type,
    }
    if node: query["query"] = node.serialize()
    if request_options := create_request_options(return_all, start, rows):
        query["request_options"] = request_options
    return send_request(query)


def create_request_options(return_all=False, start=None, rows=None):
    """Creates a request options dictionary for the RCSB search API.
    
    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :rtype: ``dict``"""

    request_options = {}
    if return_all:
        request_options["return_all_hits"] = True
    if (start is not None) or (rows is not None):
        request_options["paginate"] = {}
        if start is not None:
            request_options["paginate"]["start"] = start
        if rows is not None:
            request_options["paginate"]["rows"] = rows
    return request_options


def send_request(query):
    """Sends a query dictionary to the RCSB search API. If a valid response is
    received, this will be returned in JSON format. Otherwise ``None`` will be
    returned.
    
    :param dict query: the query, formatted to RCSB specifications.
    :rtype: ``dict``"""

    response = requests.post(SEARCH_URL, json=query)
    if response.status_code == 200:
        return response.json()