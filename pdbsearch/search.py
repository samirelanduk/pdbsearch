import inspect
from pdbsearch.nodes import full_text_node, text_node, text_chem_node
from pdbsearch.nodes import sequence_node, seqmotif_node, structure_node
from pdbsearch.nodes import strucmotif_node, chemical_node
from pdbsearch.models import GroupNode
from pdbsearch.queries import query, _create_request_options
from pdbsearch.terms import TEXT_TERMS, TEXT_CHEM_TERMS

def search(return_type="entry", **kwargs):
    """Searches the RCSB API with multiple nodes, based on the parameters given.
    Any nodes created will be combined using an "and" operator.

    :param str term: the search term for full text search.
    :param str protein: a protein sequence or pattern.
    :param str dna: a DNA sequence or pattern.
    :param str rna: an RNA sequence or pattern.
    :param float identity: the identity cutoff for sequence search.
    :param float evalue: the evalue cutoff for sequence search.
    :param str pattern_type: the type of pattern for sequence motif search.
    :param str structure: a structure identifier for structure search.
    :param str operator: the operator for structure search.
    :param str entry: a PDB entry identifier for structure motif search.
    :param tuple residues: a tuple of residue numbers for structure motif search.
    :param float rmsd: the RMSD cutoff for structure motif search.
    :param dict exchanges: a dictionary of residue exchanges for structure motif search.
    :param str smiles: a SMILES string for chemical search.
    :param str inchi: an InChI string for chemical search.
    :param str match_type: the type of match for chemical search.
    :param str return_type: the type of data to return.
    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :param str or list[str] sort: the attribute or attributes to sort by.
    :param bool counts_only: whether to return only the count of results.
    :param list[str] content_types: the PDB types (experimental/computational).
    :param list[str] facets: RCSB aggregation terms.
    :rtype: ``dict``"""

    nodes = _get_nodes_from_kwargs(return_type, kwargs)
    option_args = inspect.signature(_create_request_options).parameters.keys()
    query_kwargs = {k: v for k, v in kwargs.items() if k in option_args}
    if len(nodes) == 1:
        return nodes[0].query(return_type, **query_kwargs)
    elif len(nodes) > 1:
        return GroupNode("and", nodes).query(return_type, **query_kwargs)
    else:
        return query(return_type, **query_kwargs)


def search_entries(**kwargs):
    """Searches the RCSB API for entries, based on the parameters given.

    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :param str or list[str] sort: the attribute or attributes to sort by.
    :param bool counts_only: whether to return only the count of results.
    :param list[str] content_types: the PDB types (experimental/computational).
    :param list[str] facets: RCSB aggregation terms.
    :rtype: ``dict``"""

    return search("entry", **kwargs)


def search_polymer_entities(**kwargs):
    """Searches the RCSB API for polymer entities, based on the parameters given.

    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :param str or list[str] sort: the attribute or attributes to sort by.
    :param bool counts_only: whether to return only the count of results.
    :param list[str] content_types: the PDB types (experimental/computational).
    :param list[str] facets: RCSB aggregation terms.
    :rtype: ``dict``"""

    return search("polymer_entity", **kwargs)


def search_non_polymer_entities(**kwargs):
    """Searches the RCSB API for non-polymer entities, based on the parameters given.

    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :param str or list[str] sort: the attribute or attributes to sort by.
    :param bool counts_only: whether to return only the count of results.
    :param list[str] content_types: the PDB types (experimental/computational).
    :param list[str] facets: RCSB aggregation terms.
    :rtype: ``dict``"""

    return search("non_polymer_entity", **kwargs)


def search_polymers(**kwargs):
    """Searches the RCSB API for polymer instances, based on the parameters
    given.

    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :param str or list[str] sort: the attribute or attributes to sort by.
    :param bool counts_only: whether to return only the count of results.
    :param list[str] content_types: the PDB types (experimental/computational).
    :param list[str] facets: RCSB aggregation terms.
    :rtype: ``dict``"""

    return search("polymer_instance", **kwargs)


def search_assemblies(**kwargs):
    """Searches the RCSB API for assemblies, based on the parameters given.

    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :param str or list[str] sort: the attribute or attributes to sort by.
    :param bool counts_only: whether to return only the count of results.
    :param list[str] content_types: the PDB types (experimental/computational).
    :param list[str] facets: RCSB aggregation terms.
    :rtype: ``dict``"""

    return search("assembly", **kwargs)


def search_mols(**kwargs):
    """Searches the RCSB API for chemical structures, based on the parameters
    given.

    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :param str or list[str] sort: the attribute or attributes to sort by.
    :param bool counts_only: whether to return only the count of results.
    :param list[str] content_types: the PDB types (experimental/computational).
    :param list[str] facets: RCSB aggregation terms.
    :rtype: ``dict``"""

    return search("mol_definition", **kwargs)


def _get_nodes_from_kwargs(return_type, kwargs):
    """Generates nodes from the keyword arguments passed to the search function.

    In some cases it will need to make educated guesses about which service is
    required, based on the return type, and accompanying keyword arguments.

    :param str return_type: the type of data to return.
    :param kwargs: the parameters to use for the search.
    :rtype: ``list`` of ``TerminalNode``"""

    nodes = []
    is_mol = return_type in ["mol_definition", "non_polymer_entity"]
    for key, value in kwargs.items():
        dot_key = key.replace("__", ".")
        if key == "term":
            nodes.append(full_text_node(value))
        elif is_mol and any(dot_key.startswith(term) for term in TEXT_CHEM_TERMS):
            nodes.append(text_chem_node(**{key: value}))
        elif any(dot_key.startswith(term) for term in TEXT_TERMS):
            nodes.append(text_node(**{key: value}))
        elif key in ["protein", "dna", "rna"]:
            if "pattern_type" in kwargs:
                nodes.append(seqmotif_node(
                    pattern_type=kwargs["pattern_type"], **{key: value}
                ))
            else:
                sequence_kwargs = {
                    key: value,
                    "identity": kwargs.get("identity"),
                    "evalue": kwargs.get("evalue")
                }
                nodes.append(sequence_node(**sequence_kwargs))
        elif key == "structure":
            nodes.append(structure_node(value, operator=kwargs.get("operator")))
        elif key == "entry":
            nodes.append(strucmotif_node(
                value,
                residues=kwargs.get("residues"),
                rmsd=kwargs.get("rmsd"),
                exchanges=kwargs.get("exchanges")
            ))
        elif key == "smiles" or key == "inchi":
            chem_kwargs = {key: value}
            if mt := kwargs.get("match_type"): chem_kwargs["match_type"] = mt
            nodes.append(chemical_node(**chem_kwargs))
    return nodes