import os
from pdbsearch.schema import update_terms_from_api
from pdbsearch.queries import query
from pdbsearch.nodes import full_text_node, text_node, text_chem_node
from pdbsearch.nodes import sequence_node, seqmotif_node, structure_node
from pdbsearch.nodes import strucmotif_node, chemical_node
from pdbsearch.search import search, search_entries, search_polymer_entities
from pdbsearch.search import search_non_polymer_entities, search_polymers
from pdbsearch.search import search_assemblies, search_mols

if not os.environ.get("PDBSEARCH_NO_UPDATE"):
    update_terms_from_api()

__version__ = "0.5.0"
__author__ = "Sam Ireland"