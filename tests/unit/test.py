from unittest import TestCase
from unittest.mock import patch, Mock
from pdbsearch import full_text_node, text_node, text_chem_node, sequence_node, search, send_request, create_request_options, get_text_parameters, SEARCH_URL

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
    

    def tearDown(self):
        self.patch1.stop()
    

    def test_can_send_request(self):
        result = send_request({1: 2})
        self.mock_post.assert_called_once_with(SEARCH_URL, json={1: 2})
        self.assertEqual(result, {"result_set": [{"identifier": 1}, {"identifier": 2}, {"identifier": 3}]})
    

    def test_can_send_request_with_none_response(self):
        self.mock_post.return_value.status_code = 204
        result = send_request({1: 2})
        self.mock_post.assert_called_once_with(SEARCH_URL, json={1: 2})
        self.assertIsNone(result)