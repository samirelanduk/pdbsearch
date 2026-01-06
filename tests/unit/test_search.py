from unittest import TestCase
from unittest.mock import patch, Mock, call
from pdbsearch.search import search, search_entries, search_polymer_entities
from pdbsearch.search import search_non_polymer_entities, search_polymers
from pdbsearch.search import search_assemblies, search_mols, get_nodes_from_kwargs

class SearchTests(TestCase):

    @patch("pdbsearch.search.get_nodes_from_kwargs")
    def test_can_use_one_node(self, mock_get_nodes):
        node = Mock()
        mock_get_nodes.return_value = [node]
        result = search("entry", term="thymidine kinase")
        self.assertEqual(result, node.query.return_value)
        node.query.assert_called_once_with("entry")
        mock_get_nodes.assert_called_once_with("entry", {"term": "thymidine kinase"})
    

    @patch("pdbsearch.search.get_nodes_from_kwargs")
    def test_can_use_one_node_with_request_options(self, mock_get_nodes):
        node = Mock()
        mock_get_nodes.return_value = [node]
        result = search("entry", term="thymidine kinase", start=10, rows=20)
        self.assertEqual(result, node.query.return_value)
        node.query.assert_called_once_with("entry", start=10, rows=20)
        mock_get_nodes.assert_called_once_with("entry", {"term": "thymidine kinase", "start": 10, "rows": 20})
    

    @patch("pdbsearch.search.get_nodes_from_kwargs")
    @patch("pdbsearch.search.GroupNode")
    def test_can_use_multiple_nodes(self, mock_group_node, mock_get_nodes):
        nodes = [Mock(), Mock()]
        group_node = Mock()
        mock_group_node.return_value = group_node
        mock_get_nodes.return_value = nodes
        result = search("entry", term="thymidine kinase")
        self.assertEqual(result, group_node.query.return_value)
        group_node.query.assert_called_once_with("entry")
        mock_group_node.assert_called_once_with("and", nodes)
        mock_get_nodes.assert_called_once_with("entry", {"term": "thymidine kinase"})
    

    @patch("pdbsearch.search.get_nodes_from_kwargs")
    @patch("pdbsearch.search.GroupNode")
    def test_can_use_multiple_nodes_with_request_options(self, mock_group_node, mock_get_nodes):
        nodes = [Mock(), Mock()]
        group_node = Mock()
        mock_group_node.return_value = group_node
        mock_get_nodes.return_value = nodes
        result = search("entry", term="thymidine kinase", start=10, rows=20)
        self.assertEqual(result, group_node.query.return_value)
        group_node.query.assert_called_once_with("entry", start=10, rows=20)
        mock_group_node.assert_called_once_with("and", nodes)
        mock_get_nodes.assert_called_once_with("entry", {"term": "thymidine kinase", "start": 10, "rows": 20})
    

    @patch("pdbsearch.search.get_nodes_from_kwargs")
    @patch("pdbsearch.search.query")
    def test_can_use_no_nodes(self, mock_query, mock_get_nodes):
        mock_get_nodes.return_value = []
        result = search("entry", term="thymidine kinase")
        self.assertEqual(result, mock_query.return_value)
        mock_query.assert_called_once_with("entry")
        mock_get_nodes.assert_called_once_with("entry", {"term": "thymidine kinase"})
    

    @patch("pdbsearch.search.get_nodes_from_kwargs")
    @patch("pdbsearch.search.query")
    def test_can_use_no_nodes_with_request_options(self, mock_query, mock_get_nodes):
        mock_get_nodes.return_value = []
        result = search("entry", term="thymidine kinase", start=10, rows=20)
        self.assertEqual(result, mock_query.return_value)
        mock_query.assert_called_once_with("entry", start=10, rows=20)
        mock_get_nodes.assert_called_once_with("entry", {"term": "thymidine kinase", "start": 10, "rows": 20})



class SearchEntriesTests(TestCase):

    @patch("pdbsearch.search.search")
    def test_can_search_entries(self, mock_search):
        result = search_entries(term="thymidine kinase")
        self.assertEqual(result, mock_search.return_value)
        mock_search.assert_called_once_with("entry", term="thymidine kinase")



class SearchPolymerEntitiesTests(TestCase):

    @patch("pdbsearch.search.search")
    def test_can_search_polymer_entities(self, mock_search):
        result = search_polymer_entities(term="thymidine kinase")
        self.assertEqual(result, mock_search.return_value)
        mock_search.assert_called_once_with("polymer_entity", term="thymidine kinase")



class SearchNonPolymerEntitiesTests(TestCase):

    @patch("pdbsearch.search.search")
    def test_can_search_non_polymer_entities(self, mock_search):
        result = search_non_polymer_entities(term="thymidine kinase")
        self.assertEqual(result, mock_search.return_value)
        mock_search.assert_called_once_with("non_polymer_entity", term="thymidine kinase")



class SearchPolymersTests(TestCase):

    @patch("pdbsearch.search.search")
    def test_can_search_polymers(self, mock_search):
        result = search_polymers(term="thymidine kinase")
        self.assertEqual(result, mock_search.return_value)
        mock_search.assert_called_once_with("polymer_instance", term="thymidine kinase")



class SearchAssembliesTests(TestCase):

    @patch("pdbsearch.search.search")
    def test_can_search_assemblies(self, mock_search):
        result = search_assemblies(term="thymidine kinase")
        self.assertEqual(result, mock_search.return_value)
        mock_search.assert_called_once_with("assembly", term="thymidine kinase")



class SearchMolsTests(TestCase):

    @patch("pdbsearch.search.search")
    def test_can_search_mols(self, mock_search):
        result = search_mols(term="thymidine kinase")
        self.assertEqual(result, mock_search.return_value)
        mock_search.assert_called_once_with("mol_definition", term="thymidine kinase")



class GetNodesFromKwargsTests(TestCase):

    @patch("pdbsearch.search.full_text_node")
    def test_single_full_text_node(self, mock_full_text_node):
        nodes = get_nodes_from_kwargs("entry", {"term": "thymidine kinase"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_full_text_node.return_value)
        mock_full_text_node.assert_called_once_with("thymidine kinase")
    

    @patch("pdbsearch.search.text_node")
    def test_single_text_node(self, mock_text_node):
        nodes = get_nodes_from_kwargs("entry", {"reflns__data_reduction_details__contains": "thymidine kinase"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_text_node.return_value)
        mock_text_node.assert_called_once_with(reflns__data_reduction_details__contains="thymidine kinase")
    

    @patch("pdbsearch.search.text_node")
    def test_chem_attributes_default_to_text_node(self, mock_text_node):
        nodes = get_nodes_from_kwargs("entry", {"chem_comp__formula_weight__lt": 1000})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_text_node.return_value)
        mock_text_node.assert_called_once_with(chem_comp__formula_weight__lt=1000)
    

    @patch("pdbsearch.search.text_chem_node")
    def test_some_return_types_use_chem_text_node(self, mock_text_chem_node):
        for return_type in ["mol_definition", "non_polymer_entity"]:
            nodes = get_nodes_from_kwargs(return_type, {"chem_comp__formula_weight__lt": 1000})
            self.assertEqual(len(nodes), 1)
            self.assertEqual(nodes[0], mock_text_chem_node.return_value)
            mock_text_chem_node.assert_called_with(chem_comp__formula_weight__lt=1000)
    

    @patch("pdbsearch.search.sequence_node")
    def test_single_protein_sequence_node(self, mock_sequence_node):
        nodes = get_nodes_from_kwargs("entry", {"protein": "MALWMRLLPLLALLALWGPDPAAA"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_sequence_node.return_value)
        mock_sequence_node.assert_called_once_with(protein="MALWMRLLPLLALLALWGPDPAAA", identity=None, evalue=None)
    

    @patch("pdbsearch.search.sequence_node")
    def test_single_dna_sequence_node(self, mock_sequence_node):
        nodes = get_nodes_from_kwargs("entry", {"dna": "ATGC"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_sequence_node.return_value)
        mock_sequence_node.assert_called_once_with(dna="ATGC", identity=None, evalue=None)


    @patch("pdbsearch.search.sequence_node")
    def test_single_rna_sequence_node(self, mock_sequence_node):
        nodes = get_nodes_from_kwargs("entry", {"rna": "AUGC"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_sequence_node.return_value)
        mock_sequence_node.assert_called_once_with(rna="AUGC", identity=None, evalue=None)
    

    @patch("pdbsearch.search.sequence_node")
    def test_single_sequence_node_with_identity_and_evalue(self, mock_sequence_node):
        nodes = get_nodes_from_kwargs("entry", {"protein": "MALWMRLLPLLALLALWGPDPAAA", "identity": 0.95, "evalue": 0.0001})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_sequence_node.return_value)
        mock_sequence_node.assert_called_once_with(protein="MALWMRLLPLLALLALWGPDPAAA", identity=0.95, evalue=0.0001)
    

    @patch("pdbsearch.search.seqmotif_node")
    def test_single_protein_seqmotif_node(self, mock_seqmotif_node):
        nodes = get_nodes_from_kwargs("entry", {"protein": "MALWMRLLPLLALLALWGPDPAAA", "pattern_type": "simple"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_seqmotif_node.return_value)
        mock_seqmotif_node.assert_called_once_with(protein="MALWMRLLPLLALLALWGPDPAAA", pattern_type="simple")
    

    @patch("pdbsearch.search.seqmotif_node")
    def test_single_dna_seqmotif_node(self, mock_seqmotif_node):
        nodes = get_nodes_from_kwargs("entry", {"dna": "ATGC", "pattern_type": "simple"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_seqmotif_node.return_value)
        mock_seqmotif_node.assert_called_once_with(dna="ATGC", pattern_type="simple")
    

    @patch("pdbsearch.search.seqmotif_node")
    def test_single_rna_seqmotif_node(self, mock_seqmotif_node):
        nodes = get_nodes_from_kwargs("entry", {"rna": "AUGC", "pattern_type": "simple"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_seqmotif_node.return_value)
        mock_seqmotif_node.assert_called_once_with(rna="AUGC", pattern_type="simple")
    

    @patch("pdbsearch.search.structure_node")
    def test_single_structure_node(self, mock_structure_node):
        nodes = get_nodes_from_kwargs("entry", {"structure": "1abc"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_structure_node.return_value)
        mock_structure_node.assert_called_once_with("1abc", operator=None)
    

    @patch("pdbsearch.search.structure_node")
    def test_single_structure_node_with_operator(self, mock_structure_node):
        nodes = get_nodes_from_kwargs("entry", {"structure": "1abc", "operator": "relaxed_shape_match"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_structure_node.return_value)
        mock_structure_node.assert_called_once_with("1abc", operator="relaxed_shape_match")
    

    @patch("pdbsearch.search.strucmotif_node")
    def test_single_strucmotif_node(self, mock_strucmotif_node):
        nodes = get_nodes_from_kwargs("entry", {"entry": "1abc", "residues": (1, 2)})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_strucmotif_node.return_value)
        mock_strucmotif_node.assert_called_once_with("1abc", residues=(1, 2), rmsd=None, exchanges=None)
    

    @patch("pdbsearch.search.strucmotif_node")
    def test_single_strucmotif_node_with_rmsd(self, mock_strucmotif_node):
        nodes = get_nodes_from_kwargs("entry", {"entry": "1abc", "residues": (1, 2), "rmsd": 1.0})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_strucmotif_node.return_value)
        mock_strucmotif_node.assert_called_once_with("1abc", residues=(1, 2), rmsd=1.0, exchanges=None)
    

    @patch("pdbsearch.search.strucmotif_node")
    def test_single_strucmotif_node_with_exchanges(self, mock_strucmotif_node):
        nodes = get_nodes_from_kwargs("entry", {"entry": "1abc", "residues": (1, 2), "exchanges": {1: "A", 2: "C"}})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_strucmotif_node.return_value)
        mock_strucmotif_node.assert_called_once_with("1abc", residues=(1, 2), rmsd=None, exchanges={1: "A", 2: "C"})
    

    @patch("pdbsearch.search.chemical_node")
    def test_single_smiles_chemical_node(self, mock_chemical_node):
        nodes = get_nodes_from_kwargs("entry", {"smiles": "CC(C)C"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_chemical_node.return_value)
        mock_chemical_node.assert_called_once_with(smiles="CC(C)C", match_type=None)
    

    @patch("pdbsearch.search.chemical_node")
    def test_single_inchi_chemical_node(self, mock_chemical_node):
        nodes = get_nodes_from_kwargs("entry", {"inchi": "InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_chemical_node.return_value)
        mock_chemical_node.assert_called_once_with(inchi="InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2", match_type=None)
    

    @patch("pdbsearch.search.chemical_node")
    def test_single_chemical_node_with_match_type(self, mock_chemical_node):
        nodes = get_nodes_from_kwargs("entry", {"smiles": "CC(C)C", "match_type": "graph-relaxed-stereo"})
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], mock_chemical_node.return_value)
        mock_chemical_node.assert_called_once_with(smiles="CC(C)C", match_type="graph-relaxed-stereo")
    

    @patch("pdbsearch.search.full_text_node")
    @patch("pdbsearch.search.text_node")
    @patch("pdbsearch.search.text_chem_node")
    @patch("pdbsearch.search.sequence_node")
    @patch("pdbsearch.search.structure_node")
    @patch("pdbsearch.search.strucmotif_node")
    @patch("pdbsearch.search.chemical_node")
    def test_can_get_multiple_nodes(self, mock_chemical_node, mock_strucmotif_node, mock_structure_node, mock_sequence_node, mock_text_chem_node, mock_text_node, mock_full_text_node):
        nodes = get_nodes_from_kwargs("mol_definition", {
            "term": "thymidine kinase",
            "chem_comp__formula_weight__lt": 1000,
            "pdbx_struct_assembly__details": "good",
            "protein": "MALWMRLLPLLALLALWGPDPAAA",
            "dna": "ATGC",
            "rna": "AUGC",
            "evalue": 0.0001,
            "identity": 0.95,
            "structure": "1abc",
            "operator": "relaxed_shape_match",
            "entry": "1abc",
            "residues": (1, 2),
            "rmsd": 1.0,
            "exchanges": {1: "A", 2: "C"},
            "smiles": "CC(C)C",
            "inchi": "InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2",
            "match_type": "graph-relaxed-stereo",
        })
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes[0], mock_full_text_node.return_value)
        self.assertEqual(nodes[1], mock_text_chem_node.return_value)
        self.assertEqual(nodes[2], mock_text_node.return_value)
        self.assertEqual(nodes[3], mock_sequence_node.return_value)
        self.assertEqual(nodes[4], mock_sequence_node.return_value)
        self.assertEqual(nodes[5], mock_sequence_node.return_value)
        self.assertEqual(nodes[6], mock_structure_node.return_value)
        self.assertEqual(nodes[7], mock_strucmotif_node.return_value)
        self.assertEqual(nodes[8], mock_chemical_node.return_value)
        self.assertEqual(nodes[9], mock_chemical_node.return_value)
        mock_full_text_node.assert_called_once_with("thymidine kinase")
        mock_text_chem_node.assert_called_once_with(chem_comp__formula_weight__lt=1000)
        mock_text_node.assert_called_once_with(pdbx_struct_assembly__details="good")
        mock_sequence_node.assert_has_calls([
            call(protein="MALWMRLLPLLALLALWGPDPAAA", identity=0.95, evalue=0.0001),
            call(dna="ATGC", identity=0.95, evalue=0.0001),
            call(rna="AUGC", identity=0.95, evalue=0.0001),
        ])
        mock_structure_node.assert_called_once_with("1abc", operator="relaxed_shape_match")
        mock_strucmotif_node.assert_called_once_with("1abc", residues=(1, 2), rmsd=1.0, exchanges={1: "A", 2: "C"})
        mock_chemical_node.assert_has_calls([
            call(smiles="CC(C)C", match_type="graph-relaxed-stereo"),
            call(inchi="InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2", match_type="graph-relaxed-stereo"),
        ])
    
    




    
    