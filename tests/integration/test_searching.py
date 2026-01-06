from unittest import TestCase
from unittest.mock import patch
import pdbsearch

class SearchTestCase(TestCase):

    def setUp(self):
        self.patch1 = patch("requests.post")
        self.mock_post = self.patch1.start()
        self.mock_post.return_value.status_code = 200

    def tearDown(self):
        self.patch1.stop()


class SearchTests(SearchTestCase):

    def test_can_search_default(self):
        result = pdbsearch.search()
        self.assertEqual(result, self.mock_post.return_value.json.return_value)
        self.mock_post.assert_called_once_with(
            "https://search.rcsb.org/rcsbsearch/v2/query",
            json={"return_type": "entry"}
        )
    

    def test_can_search_complex_query(self):
        result = pdbsearch.search(
            return_type="polymer_entity",
            term="thymidine kinase",
            chem_comp__formula_weight__lt=1000,
            pdbx_struct_assembly__details__not__contains="good",
            protein="MALWMRLLPLLALLALWGPDPAAA",
            dna="ATGC",
            rna="AUGC",
            identity=0.95,
            evalue=1e-10,
            structure="1A2B-2",
            operator="relaxed_shape_match",
            entry="1A2B",
            residues=(("A", 1), ("B", 2)),
            rmsd=0.5,
            exchanges={("A", 1): ["ASP"], ("B", 2): ["HIS"]},
            smiles="CC(C)C",
            inchi="InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2",
            match_type="graph-relaxed-stereo",
            start=10,
            rows=20,
            sort=["-rcsb_accession_info.deposit_date", "rcsb_assembly_info.polymer_entity_count"],
            counts_only=True,
            content_types=["experimental", "computational"],
        )
        self.assertEqual(result, self.mock_post.return_value.json.return_value)
        self.mock_post.assert_called_once_with(
            "https://search.rcsb.org/rcsbsearch/v2/query",
            json={
                "return_type": "polymer_entity",
                "query": {
                    "type": "group", "logical_operator": "and", "nodes": [
                        {"type": "terminal", "service": "full_text", "parameters": {"value": "thymidine kinase"}},
                        {"type": "terminal", "service": "text", "parameters": {"attribute": "chem_comp.formula_weight", "operator": "less", "value": 1000}},
                        {"type": "terminal", "service": "text", "parameters": {"attribute": "pdbx_struct_assembly.details", "operator": "contains_phrase", "value": "good", "negation": True}},
                        {"type": "terminal", "service": "sequence", "parameters": {"sequence_type": "protein", "value": "MALWMRLLPLLALLALWGPDPAAA", "identity_cutoff": 0.95, "evalue_cutoff": 1e-10}},
                        {"type": "terminal", "service": "sequence", "parameters": {"sequence_type": "dna", "value": "ATGC", "identity_cutoff": 0.95, "evalue_cutoff": 1e-10}},
                        {"type": "terminal", "service": "sequence", "parameters": {"sequence_type": "rna", "value": "AUGC", "identity_cutoff": 0.95, "evalue_cutoff": 1e-10}},
                        {"type": "terminal", "service": "structure", "parameters": {"value": {"entry_id": "1A2B", "assembly_id": "2"}, "operator": "relaxed_shape_match"}},
                        {"type": "terminal", "service": "strucmotif", "parameters": {
                            "value": {"entry_id": "1A2B", "residue_ids": [{"label_asym_id": "A", "label_seq_id": 1}, {"label_asym_id": "B", "label_seq_id": 2}]},
                            "rmsd_cutoff": 0.5,
                            "exchanges": [{"residue_id": {"label_asym_id": "A", "label_seq_id": 1}, "allowed": ["ASP"]}, {"residue_id": {"label_asym_id": "B", "label_seq_id": 2}, "allowed": ["HIS"]}]
                        }},
                        {"type": "terminal", "service": "chemical", "parameters": {"value": "CC(C)C", "type": "descriptor", "descriptor_type": "SMILES", "match_type": "graph-relaxed-stereo"}},
                        {"type": "terminal", "service": "chemical", "parameters": {"value": "InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2", "type": "descriptor", "descriptor_type": "InChI", "match_type": "graph-relaxed-stereo"}}
                    ]},
                "request_options": {
                    "paginate": {"start": 10, "rows": 20},
                    "sort": [{"sort_by": "rcsb_accession_info.deposit_date", "direction": "desc"}, {"sort_by": "rcsb_assembly_info.polymer_entity_count", "direction": "asc"}],
                    "return_counts": True,
                    "results_content_type": ["experimental", "computational"]
                }
            }
        )



class QueryTests(SearchTestCase):

    def test_one_node(self):
        node = pdbsearch.text_node(rcsb_target_neighbors__distance__range=(10, 20))
        result = node.query("mol_definition")
        self.assertEqual(result, self.mock_post.return_value.json.return_value)
        self.mock_post.assert_called_once_with(
            "https://search.rcsb.org/rcsbsearch/v2/query",
            json={
                "return_type": "mol_definition",
                "query": {"type": "terminal", "service": "text", "parameters": {
                    "attribute": "rcsb_target_neighbors.distance",
                    "operator": "range",
                    "value": {"from": 10, "to": 20, "include_lower": False, "include_upper": False}
                }},
            }
        )
    

    def test_multiple_nodes(self):
        node1 = pdbsearch.text_node(rcsb_target_neighbors__distance__not__range=[10, 20])
        node2 = pdbsearch.text_chem_node(chem_comp__formula_weight__lt=1000)
        node3 = pdbsearch.full_text_node("thymidine kinase")
        node4 = pdbsearch.sequence_node(protein="MALWMRLLPLLALLALWGPDPAAA", identity=0.95, evalue=1e-10)
        node5 = pdbsearch.sequence_node(dna="ATGC", identity=0.95, evalue=1e-10)
        node6 = pdbsearch.sequence_node(rna="AUGC", identity=0.95, evalue=1e-10)
        node7 = pdbsearch.seqmotif_node(protein="PSSM", pattern_type="motif")
        node8 = pdbsearch.structure_node("1A2B-2", operator="relaxed_shape_match")
        node9 = pdbsearch.strucmotif_node("1A2B-2", residues=(("A", 1), ("B", 2)), rmsd=0.5, exchanges={("A", 1): ["ASP"], ("B", 2): ["HIS"]})
        node10 = pdbsearch.chemical_node(smiles="CC(C)C", match_type="graph-relaxed-stereo")
        node11 = pdbsearch.chemical_node(inchi="InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2", match_type="graph-relaxed-stereo")
        node = (node1.or_(node2).and_(node3)).or_(node4.or_(node5.or_(node6))).and_(node7).or_(node8.and_(node9)).or_(node10.or_(node11))
        result = node.query("mol_definition", return_all=True)
        self.assertEqual(result, self.mock_post.return_value.json.return_value)
        self.mock_post.assert_called_once_with(
            "https://search.rcsb.org/rcsbsearch/v2/query",
            json={
                "return_type": "mol_definition",
                "query": {
                    "type": "group", "logical_operator": "or", "nodes": [{
                        "type": "group", "logical_operator": "and", "nodes": [{
                            "type": "group", "logical_operator": "or", "nodes": [{
                                "type": "group", "logical_operator": "and", "nodes": [{
                                    "type": "group", "logical_operator": "or", "nodes": [
                                        {"type": "terminal", "service": "text", "parameters": {"attribute": "rcsb_target_neighbors.distance", "operator": "range", "value": {"from": 10, "to": 20, "include_lower": True, "include_upper": True}, "negation": True}},
                                        {"type": "terminal", "service": "text_chem", "parameters": {"attribute": "chem_comp.formula_weight", "operator": "less", "value": 1000}}
                                    ]}, {
                                        "type": "terminal", "service": "full_text", "parameters": {"value": "thymidine kinase"}}
                                    ]}, {
                                        "type": "group", "logical_operator": "or", "nodes": [
                                            {"type": "terminal", "service": "sequence", "parameters": {"sequence_type": "protein", "value": "MALWMRLLPLLALLALWGPDPAAA", "identity_cutoff": 0.95, "evalue_cutoff": 1e-10}},
                                            {"type": "terminal", "service": "sequence", "parameters": {"sequence_type": "dna", "value": "ATGC", "identity_cutoff": 0.95, "evalue_cutoff": 1e-10}},
                                            {"type": "terminal", "service": "sequence", "parameters": {"sequence_type": "rna", "value": "AUGC", "identity_cutoff": 0.95, "evalue_cutoff": 1e-10}}
                                        ]}
                                    ]}, {
                                        "type": "terminal", "service": "seqmotif", "parameters": {"value": "PSSM", "pattern_type": "motif", "sequence_type": "protein"}}
                                    ]}, {"type": "group", "logical_operator": "and", "nodes": [
                                        {"type": "terminal", "service": "structure", "parameters": {"value": {"entry_id": "1A2B", "assembly_id": "2"}, "operator": "relaxed_shape_match"}},
                                        {"type": "terminal", "service": "strucmotif", "parameters": {"value": {"entry_id": "1A2B-2", "residue_ids": [{"label_asym_id": "A", "label_seq_id": 1}, {"label_asym_id": "B", "label_seq_id": 2}]}, "rmsd_cutoff": 0.5, "exchanges": [{"residue_id": {"label_asym_id": "A", "label_seq_id": 1}, "allowed": ["ASP"]}, {"residue_id": {"label_asym_id": "B", "label_seq_id": 2}, "allowed": ["HIS"]}
                                    ]}
                                }]
                            },
                            {"type": "terminal", "service": "chemical", "parameters": {"value": "CC(C)C", "type": "descriptor", "descriptor_type": "SMILES", "match_type": "graph-relaxed-stereo"}},
                            {"type": "terminal", "service": "chemical", "parameters": {"value": "InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2", "type": "descriptor", "descriptor_type": "InChI", "match_type": "graph-relaxed-stereo"}}
                        ]},
                "request_options": {"return_all_hits": True}
            })