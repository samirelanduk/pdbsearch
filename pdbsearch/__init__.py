import os
from pdbsearch.schema import update_terms_from_api
from pdbsearch.queries import search
from pdbsearch.nodes import full_text_node, text_node, text_chem_node
from pdbsearch.nodes import sequence_node, seqmotif_node, structure_node
from pdbsearch.nodes import strucmotif_node, chemical_node

if not os.environ.get("PDBSEARCH_NO_UPDATE"):
    update_terms_from_api()