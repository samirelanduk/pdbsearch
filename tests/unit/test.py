import io
import sys
import requests
from unittest import TestCase
from unittest.mock import patch, Mock
from pdbsearch import full_text_node, text_node, text_chem_node, sequence_node, seqmotif_node, structure_node, strucmotif_node, chemical_node, search, send_request, create_request_options, get_text_parameters, SEARCH_URL

class FullTextNodeTests(TestCase):

    def test_can_create_full_text_node(self):
        node = full_text_node("thymidine kinase")
        self.assertEqual(node.service, "full_text")
        self.assertEqual(node.parameters, {"value": "thymidine kinase"})



class TextNodeTests(TestCase):

    @patch("pdbsearch.get_text_parameters")
    def test_can_create_text_node(self, mock_get_text_parameters):
        mock_get_text_parameters.return_value = {1: 2}
        node = text_node(name="xxx")
        self.assertEqual(node.service, "text")
        self.assertEqual(node.parameters, {1: 2})
        mock_get_text_parameters.assert_called_once_with("name", "xxx")
    

    def test_cant_have_zero_arguments(self):
        with self.assertRaises(ValueError):
            text_node()
    

    def test_cant_have_multiple_arguments(self):
        with self.assertRaises(ValueError):
            text_node(name="xxx", name2="yyy")



class ChemTextNodeTests(TestCase):

    @patch("pdbsearch.get_text_parameters")
    def test_can_create_chem_text_node(self, mock_get_text_parameters):
        mock_get_text_parameters.return_value = {1: 2}
        node = text_chem_node(name="xxx")
        self.assertEqual(node.service, "text_chem")
        self.assertEqual(node.parameters, {1: 2})
        mock_get_text_parameters.assert_called_once_with("name", "xxx", text_chem=True)
    

    def test_cant_have_zero_arguments(self):
        with self.assertRaises(ValueError):
            text_chem_node()
    

    def test_cant_have_multiple_arguments(self):
        with self.assertRaises(ValueError):
            text_chem_node(name="xxx", name2="yyy")



class SequenceNodeTests(TestCase):

    def test_can_create_protein_sequence_node(self):
        node = sequence_node(protein="MALWMRLLPLLALLALWGPDPAAA")
        self.assertEqual(node.service, "sequence")
        self.assertEqual(node.parameters, {"sequence_type": "protein", "value": "MALWMRLLPLLALLALWGPDPAAA"})
    

    def test_can_create_dna_sequence_node(self):
        node = sequence_node(dna="ATGC")
        self.assertEqual(node.service, "sequence")
        self.assertEqual(node.parameters, {"sequence_type": "dna", "value": "ATGC"})
    

    def test_can_create_rna_sequence_node(self):
        node = sequence_node(rna="AUGC")
        self.assertEqual(node.service, "sequence")
        self.assertEqual(node.parameters, {"sequence_type": "rna", "value": "AUGC"})
    

    def test_can_provide_identity_cutoff(self):
        node = sequence_node(protein="MALWMRLLPLLALLALWGPDPAAA", identity=0.95)
        self.assertEqual(node.service, "sequence")
        self.assertEqual(node.parameters, {"sequence_type": "protein", "value": "MALWMRLLPLLALLALWGPDPAAA", "identity_cutoff": 0.95})
    

    def test_can_provide_evalue_cutoff(self):
        node = sequence_node(protein="MALWMRLLPLLALLALWGPDPAAA", evalue=0.0001)
        self.assertEqual(node.service, "sequence")
        self.assertEqual(node.parameters, {"sequence_type": "protein", "value": "MALWMRLLPLLALLALWGPDPAAA", "evalue_cutoff": 0.0001})
    

    def test_cant_have_zero_sequences(self):
        with self.assertRaises(ValueError):
            sequence_node()
    

    def test_cant_have_multiple_sequences(self):
        with self.assertRaises(ValueError):
            sequence_node(protein="MALWMRLLPLLALLALWGPDPAAA", dna="ATGC")



class SeqMotifNodeTests(TestCase):

    def test_can_create_protein_seqmotif_node(self):
        node = seqmotif_node(protein="MALWMRLLPLLALLALWGPDPAAA", pattern_type="simple")
        self.assertEqual(node.service, "seqmotif")
        self.assertEqual(node.parameters, {"pattern_type": "simple", "value": "MALWMRLLPLLALLALWGPDPAAA", "sequence_type": "protein"})
    

    def test_can_create_dna_seqmotif_node(self):
        node = seqmotif_node(dna="ATGC", pattern_type="simple")
        self.assertEqual(node.service, "seqmotif")
        self.assertEqual(node.parameters, {"pattern_type": "simple", "value": "ATGC", "sequence_type": "dna"})
    

    def test_can_create_rna_seqmotif_node(self):
        node = seqmotif_node(rna="AUGC", pattern_type="simple")
        self.assertEqual(node.service, "seqmotif")
        self.assertEqual(node.parameters, {"pattern_type": "simple", "value": "AUGC", "sequence_type": "rna"})
    

    def test_cant_have_zero_patterns(self):
        with self.assertRaises(ValueError):
            seqmotif_node()
    

    def test_cant_have_multiple_patterns(self):
        with self.assertRaises(ValueError):
            seqmotif_node(protein="MALWMRLLPLLALLALWGPDPAAA", dna="ATGC")



class StructureNodeTests(TestCase):

    def test_can_get_by_entry(self):
        node = structure_node("1CLL-5")
        self.assertEqual(node.service, "structure")
        self.assertEqual(node.parameters, {"value": {"entry_id": "1CLL", "assembly_id": "5"}, "operator": "strict_shape_match"})
    

    def test_can_get_by_url(self):
        node = structure_node("https://alphafold.ebi.ac.uk/AFP61371F1.cif")
        self.assertEqual(node.service, "structure")
        self.assertEqual(node.parameters, {"value": {"url": "https://alphafold.ebi.ac.uk/AFP61371F1.cif", "format": "cif"}, "operator": "strict_shape_match"})
    

    def test_can_get_by_bcif_url(self):
        node = structure_node("https://alphafold.ebi.ac.uk/AFP61371F1.bcif")
        self.assertEqual(node.service, "structure")
        self.assertEqual(node.parameters, {"value": {"url": "https://alphafold.ebi.ac.uk/AFP61371F1.bcif", "format": "bcif"}, "operator": "strict_shape_match"})
    

    def test_can_change_operator(self):
        node = structure_node("1CLL-5", "relaxed_shape_match")
        self.assertEqual(node.service, "structure")
        self.assertEqual(node.parameters, {"value": {"entry_id": "1CLL", "assembly_id": "5"}, "operator": "relaxed_shape_match"})
    

    def test_entry_must_be_in_format_entry_assembly(self):
        with self.assertRaises(ValueError):
            structure_node("1CLL")
    

    
class StrucMotifNodeTests(TestCase):

    def test_can_create_strucmotif_node(self):
        node = strucmotif_node("2mnr", residues=(("A", 162), ("A", 193), ("A", 219)))
        self.assertEqual(node.service, "strucmotif")
        self.assertEqual(node.parameters, {"value": {"entry_id": "2mnr", "residue_ids": [{"label_asym_id": "A", "label_seq_id": 162}, {"label_asym_id": "A", "label_seq_id": 193}, {"label_asym_id": "A", "label_seq_id": 219}]}})
    

    def test_can_create_strucmotif_node_with_rmsd(self):
        node = strucmotif_node("2mnr", residues=(("A", 162), ("A", 193), ("A", 219)), rmsd=2)
        self.assertEqual(node.service, "strucmotif")
        self.assertEqual(node.parameters, {"value": {"entry_id": "2mnr", "residue_ids": [{"label_asym_id": "A", "label_seq_id": 162}, {"label_asym_id": "A", "label_seq_id": 193}, {"label_asym_id": "A", "label_seq_id": 219}]}, "rmsd_cutoff": 2})
    

    def test_can_create_strucmotif_node_with_exchanges(self):
        node = strucmotif_node("2mnr", residues=(("A", 162), ("A", 193), ("A", 219)), exchanges={
            ("A", 162): ["LYS", "HIS"],
            ("A", 245): ["GLU", "ASP", "ASN"],
            ("A", 295): ["HIS", "LYS"]
        })
        self.assertEqual(node.service, "strucmotif")
        self.assertEqual(node.parameters, {
            "value": {
                "entry_id": "2mnr",
                "residue_ids": [{"label_asym_id": "A", "label_seq_id": 162}, {"label_asym_id": "A", "label_seq_id": 193}, {"label_asym_id": "A", "label_seq_id": 219}]},
                "exchanges": [{"residue_id": {"label_asym_id": "A", "label_seq_id": 162}, "allowed": ["LYS", "HIS"]}, {"residue_id": {"label_asym_id": "A", "label_seq_id": 245}, "allowed": ["GLU", "ASP", "ASN"]}, {"residue_id": {"label_asym_id": "A", "label_seq_id": 295}, "allowed": ["HIS", "LYS"]}]
            })



class ChemicalNodeTests(TestCase):

    def test_can_create_smiles_chemical_node(self):
        node = chemical_node(smiles="CC(C)C")
        self.assertEqual(node.service, "chemical")
        self.assertEqual(node.parameters, {"value": "CC(C)C", "type": "descriptor", "descriptor_type": "SMILES", "match_type": "graph-exact"})
    

    def test_can_create_inchi_chemical_node(self):
        node = chemical_node(inchi="InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2")
        self.assertEqual(node.service, "chemical")
        self.assertEqual(node.parameters, {"value": "InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2", "type": "descriptor", "descriptor_type": "InChI", "match_type": "graph-exact"})
    

    def test_must_provide_one_of_smiles_or_inchi(self):
        with self.assertRaises(ValueError):
            chemical_node()
    

    def test_cant_provide_both_smiles_and_inchi(self):
        with self.assertRaises(ValueError):
            chemical_node(smiles="CC(C)C", inchi="InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2")
    

    def test_can_change_match_type(self):
        node = chemical_node(smiles="CC(C)C", match_type="graph-relaxed-stereo")
        self.assertEqual(node.service, "chemical")
        self.assertEqual(node.parameters, {"value": "CC(C)C", "type": "descriptor", "descriptor_type": "SMILES", "match_type": "graph-relaxed-stereo"})



class GetTextParametersTests(TestCase):

    def test_exact_match(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name", "xxx")
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "exact_match", "value": "xxx"})
    

    def test_not_exact_match(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__not", "xxx")
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "exact_match", "negation": True, "value": "xxx"})


    def test_equals(self):
        parameters = get_text_parameters("refine__B_iso_mean", 123)
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "equals", "value": 123})
    

    def test_not_equals(self):
        parameters = get_text_parameters("refine__B_iso_mean__not", 123)
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "equals", "negation": True, "value": 123})
    

    def test_greater_than(self):
        parameters = get_text_parameters("refine__B_iso_mean__gt", 123)
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "greater_than", "value": 123})


    def test_not_greater_than(self):
        parameters = get_text_parameters("refine__B_iso_mean__not__gt", 123)
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "greater_than", "negation": True, "value": 123})


    def test_less_than(self):
        parameters = get_text_parameters("refine__B_iso_mean__lt", 123)
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "less_than", "value": 123})


    def test_not_less_than(self):
        parameters = get_text_parameters("refine__B_iso_mean__not__lt", 123)
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "less_than", "negation": True, "value": 123})
    

    def test_greater_or_equal(self):
        parameters = get_text_parameters("refine__B_iso_mean__gte", 123)
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "greater_or_equal", "value": 123})


    def test_not_greater_or_equal(self):
        parameters = get_text_parameters("refine__B_iso_mean__not__gte", 123)
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "greater_or_equal", "negation": True, "value": 123})


    def test_less_or_equal(self):
        parameters = get_text_parameters("refine__B_iso_mean__lte", 123)
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "less_or_equal", "value": 123})


    def test_not_less_or_equal(self):
        parameters = get_text_parameters("refine__B_iso_mean__not__lte", 123)
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "less_or_equal", "negation": True, "value": 123})


    def test_in(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__in", ["xxx", "yyy"])
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "in", "value": ["xxx", "yyy"]})


    def test_not_in(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__not__in", ["xxx", "yyy"])
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "in", "negation": True, "value": ["xxx", "yyy"]})


    def test_range(self):
        parameters = get_text_parameters("refine__B_iso_mean__range", [123, 456])
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "range", "value": {"from": 123, "to": 456, "include_lower": True, "include_upper": True}})


    def test_not_range(self):
        parameters = get_text_parameters("refine__B_iso_mean__not__range", [123, 456])
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "range", "negation": True, "value": {"from": 123, "to": 456, "include_lower": True, "include_upper": True}})
    

    def test_exclusive_range(self):
        parameters = get_text_parameters("refine__B_iso_mean__range", (123, 456))
        self.assertEqual(parameters, {"attribute": "refine.B_iso_mean", "operator": "range", "value": {"from": 123, "to": 456, "include_lower": False, "include_upper": False}})


    def test_contains(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__contains", "xxx")
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "contains_phrase", "value": "xxx"})


    def test_not_contains(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__not__contains", "xxx")
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "contains_phrase", "negation": True, "value": "xxx"})


    def test_contains_phrase(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__contains_phrase", "xxx")
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "contains_phrase", "value": "xxx"})


    def test_not_contains_phrase(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__not__contains_phrase", "xxx")
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "contains_phrase", "negation": True, "value": "xxx"})


    def test_contains_words(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__contains_words", "xxx")
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "contains_words", "value": "xxx"})


    def test_not_contains_words(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__not__contains_words", "xxx")
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "contains_words", "negation": True, "value": "xxx"})


    def test_exists(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__exists", True)
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "exists"})


    def test_not_exists(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__not__exists", True)
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "exists", "negation": True})


    def test_doesnt_exist(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__exists", False)
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "exists", "negation": True})


    def test_not_doesnt_exist(self):
        parameters = get_text_parameters("pdbx_entity_nonpoly__name__not__exists", False)
        self.assertEqual(parameters, {"attribute": "pdbx_entity_nonpoly.name", "operator": "exists"})
    
    
    def test_invalid_term(self):
        with self.assertRaises(ValueError):
            get_text_parameters("pdbx_entity_nonpoly__name__invalid", "xxx")
    

    def test_can_use_chem_text_parameters(self):
        parameters = get_text_parameters("chem_comp__formula_weight__lt", 1000, text_chem=True)
        self.assertEqual(parameters, {"attribute": "chem_comp.formula_weight", "operator": "less_than", "value": 1000})



class SearchTests(TestCase):

    @patch("pdbsearch.create_request_options")
    @patch("pdbsearch.send_request")
    def test_minimal_search(self, mock_send_request, mock_create_request_options):
        mock_create_request_options.return_value = {}
        result = search("entry")
        mock_send_request.assert_called_once_with({"return_type": "entry"})
        self.assertEqual(result, mock_send_request.return_value)


    @patch("pdbsearch.create_request_options")
    @patch("pdbsearch.send_request")
    def test_can_search_with_node(self, mock_send_request, mock_create_request_options):
        mock_create_request_options.return_value = {}
        node = Mock()
        result = search("entry", node=node)
        mock_send_request.assert_called_once_with({"return_type": "entry", "query": node.serialize.return_value})
        self.assertEqual(result, mock_send_request.return_value)
    

    @patch("pdbsearch.create_request_options")
    @patch("pdbsearch.send_request")
    def test_can_search_with_options(self, mock_send_request, mock_create_request_options):
        mock_create_request_options.return_value = {"xxx": True}
        result = search("entry", return_all=True)
        mock_send_request.assert_called_once_with({"return_type": "entry", "request_options": {"xxx": True}})
        self.assertEqual(result, mock_send_request.return_value)



class CreateRequestOptionsTests(TestCase):

    def test_can_return_empty_options(self):
        result = create_request_options()
        self.assertEqual(result, {})
    

    def test_return_all_options(self):
        result = create_request_options(return_all=True)
        self.assertEqual(result, {"return_all_hits": True})


    def test_start(self):
        result = create_request_options(start=10)
        self.assertEqual(result, {"paginate": {"start": 10}})


    def test_rows(self):
        result = create_request_options(rows=10)
        self.assertEqual(result, {"paginate": {"rows": 10}})


    def test_start_and_rows(self):
        result = create_request_options(start=10, rows=5)
        self.assertEqual(result, {"paginate": {"start": 10, "rows": 5}})



class SendRequestTests(TestCase):

    def setUp(self):
        self.patch1 = patch("requests.post")
        self.mock_post = self.patch1.start()
        self.mock_post.return_value.status_code = 200
        self.mock_post.return_value.json.return_value = {"result_set": [{"identifier": 1}, {"identifier": 2}, {"identifier": 3}]}
        self.stderr = io.StringIO()
        self.old_stderr = sys.stderr
        sys.stderr = self.stderr
    

    def tearDown(self):
        self.patch1.stop()
        sys.stderr = self.old_stderr
    

    def test_can_send_request(self):
        result = send_request({1: 2})
        self.mock_post.assert_called_once_with(SEARCH_URL, json={1: 2})
        self.assertEqual(result, {"result_set": [{"identifier": 1}, {"identifier": 2}, {"identifier": 3}]})
    

    def test_can_handle_json_error_response(self):
        self.mock_post.return_value.status_code = 400
        self.mock_post.return_value.json.return_value = {"error": "Invalid request"}
        send_request({1: 2})
        self.mock_post.assert_called_once_with(SEARCH_URL, json={1: 2})
        stderr_output = self.stderr.getvalue()
        self.assertEqual(stderr_output, "{'error': 'Invalid request'}\n")
    

    def test_can_handle_short_non_json_response(self):
        self.mock_post.return_value.status_code = 400
        self.mock_post.return_value.json.side_effect = requests.exceptions.JSONDecodeError("", "", 0)
        self.mock_post.return_value.content = b"Invalid request"
        send_request({1: 2})
        self.mock_post.assert_called_once_with(SEARCH_URL, json={1: 2})
        stderr_output = self.stderr.getvalue()
        self.assertEqual(stderr_output, "400 Invalid request\n")
    

    def test_can_handle_long_non_json_response(self):
        self.mock_post.return_value.status_code = 400
        self.mock_post.return_value.json.side_effect = requests.exceptions.JSONDecodeError("", "", 0)
        self.mock_post.return_value.content = b"X" * 101
        send_request({1: 2})
        self.mock_post.assert_called_once_with(SEARCH_URL, json={1: 2})
        stderr_output = self.stderr.getvalue()
        self.assertEqual(stderr_output, "400 \n")