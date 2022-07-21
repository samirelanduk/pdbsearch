from unittest import TestCase
from unittest.mock import patch
from pdbsearch.rcsb import *

class SearchTests(TestCase):

    @patch("pdbsearch.rcsb.apply_pagination")
    @patch("pdbsearch.rcsb.apply_sort")
    @patch("pdbsearch.rcsb.apply_query")
    @patch("pdbsearch.rcsb.send_request")
    def test_successful_search(self, mock_req, mock_query, mock_sort, mock_pag):
        mock_req.return_value = {"result_set": [
            {"identifier": "1XXX"}, {"identifier": "1YYY"}
        ]}
        result = search(start=10, limit=20, sort="xxx", a=1, b=2)
        mock_pag.assert_called_with({"return_type": "entry"}, 10, 20)
        mock_sort.assert_called_with({"return_type": "entry"}, "xxx")
        mock_query.assert_called_with({"return_type": "entry"}, {"a": 1, "b": 2})
        mock_req.assert_called_with({"return_type": "entry"})
        self.assertEqual(result, ["1XXX", "1YYY"])
    

    @patch("pdbsearch.rcsb.apply_pagination")
    @patch("pdbsearch.rcsb.apply_sort")
    @patch("pdbsearch.rcsb.apply_query")
    @patch("pdbsearch.rcsb.send_request")
    def test_unsuccessful_search(self, mock_req, mock_query, mock_sort, mock_pag):
        mock_req.return_value = None
        result = search(start=10, limit=20, sort="xxx", a=1, b=2)
        mock_pag.assert_called_with({"return_type": "entry"}, 10, 20)
        mock_sort.assert_called_with({"return_type": "entry"}, "xxx")
        mock_query.assert_called_with({"return_type": "entry"}, {"a": 1, "b": 2})
        mock_req.assert_called_with({"return_type": "entry"})
        self.assertIsNone(result)




class PaginationApplyingTests(TestCase):

    def test_can_get_all_codes(self):
        query = {}
        apply_pagination(query, 0, None)
        self.assertEqual(query, {"request_options": {"return_all_hits": True}})
    

    def test_can_get_limit_codes(self):
        query = {}
        apply_pagination(query, 10, 45)
        self.assertEqual(query, {"request_options": {"paginate": {"start": 10, "rows": 45}}})


class SortApplyingTests(TestCase):

    def test_can_do_nothing(self):
        query = {"request_options": {}}
        apply_sort(query, None)
        self.assertEqual(query, {"request_options": {}})


    @patch("pdbsearch.rcsb.sort_term_to_sort_dict")
    def test_can_apply_single_sort_term(self, mock_convert):
        query = {"request_options": {}}
        mock_convert.return_value = "sort_term"
        apply_sort(query, "xxx")
        mock_convert.assert_called_with("xxx")
        self.assertEqual(query, {"request_options": {
            "sort": ["sort_term"]
        }})
    

    @patch("pdbsearch.rcsb.sort_term_to_sort_dict")
    def test_can_apply_multiple_sort_terms(self, mock_convert):
        query = {"request_options": {}}
        mock_convert.side_effect = ["sort_term1", "sort_term2"]
        apply_sort(query, ["xxx", "yyy"])
        mock_convert.assert_any_call("xxx")
        mock_convert.assert_any_call("yyy")
        self.assertEqual(query, {"request_options": {
            "sort": ["sort_term1", "sort_term2"]
        }})



class SortTermToSortDictTests(TestCase):

    def test_term_generation(self):
        self.assertEqual(sort_term_to_sort_dict("xxx"), {
            "sort_by": "xxx", "direction": "desc"
        })
    

    def test_asc_term_generation(self):
        self.assertEqual(sort_term_to_sort_dict("-xxx"), {
            "sort_by": "xxx", "direction": "asc"
        })
    

    def test_special_term_generation(self):
        self.assertEqual(sort_term_to_sort_dict("code"), {
            "sort_by": "rcsb_entry_container_identifiers.entry_id", "direction": "desc"
        })
    

    def test_asc_term_generation(self):
        self.assertEqual(sort_term_to_sort_dict("-atoms"), {
            "sort_by": "rcsb_entry_info.deposited_atom_count", "direction": "asc"
        })


class QueryApplyingTests(TestCase):

    @patch("pdbsearch.rcsb.get_query_parameters")
    def test_can_apply_criteria(self, mock_params):
        query = {}
        mock_params.side_effect = ["param1", None, "param3"]
        apply_query(query, {"key1": 1, "key2": 2, "key3": 3})
        mock_params.assert_any_call("key1", 1)
        mock_params.assert_any_call("key2", 2)
        mock_params.assert_any_call("key3", 3)
        self.assertEqual(query, {"query": {
            "type": "group", "logical_operator": "and", "nodes": [
                {"type": "terminal", "service": "text", "parameters": "param1"},
                {"type": "terminal", "service": "text", "parameters": "param3"},
            ]
        }})
    

    @patch("pdbsearch.rcsb.get_query_parameters")
    def test_can_apply_no_criteria(self, mock_params):
        query = {}
        apply_query(query, {})
        self.assertFalse(mock_params.called)
        self.assertEqual(query, {"query": {"type": "terminal", "service": "text"}})



class QueryParameterTests(TestCase):

    @patch("pdbsearch.rcsb.get_query_attribute")
    @patch("pdbsearch.rcsb.get_query_operator")
    def test_can_get_query_parameters(self, mock_op, mock_att):
        parameters = get_query_parameters("property", "value")
        mock_att.assert_called_with("property")
        mock_op.assert_called_with("property", "value")
        self.assertEqual(parameters, {
            "attribute": mock_att.return_value, "operator": mock_op.return_value,
            "value": "value"    
        })



class QueryAttributeTests(TestCase):

    def test_can_get_attribute_unmodified(self):
        self.assertEqual(get_query_attribute("some_attribute"), "some_attribute")
    

    def test_can_add_dots(self):
        self.assertEqual(get_query_attribute("some__attribute"), "some.attribute")
    

    def test_can_remove_suffixes(self):
        self.assertEqual(get_query_attribute("some_attribute__lt"), "some_attribute")
        self.assertEqual(get_query_attribute("some__attribute__gt"), "some.attribute")
    

    def test_can_apply_shorthand(self):
        self.assertEqual(get_query_attribute("ligand_name"), "rcsb_nonpolymer_instance_feature_summary.comp_id")
        self.assertEqual(get_query_attribute("ligand_distance__lt"), "rcsb_ligand_neighbors.distance")



class QueryOperatorTests(TestCase):

    def test_can_get_exact_match_operator(self):
        self.assertEqual(get_query_operator("key1", "abc"), "exact_match")
    

    def test_can_get_equals_operator(self):
        self.assertEqual(get_query_operator("key1", 10), "equals")
        self.assertEqual(get_query_operator("key1", 10.5), "equals")
    

    def test_can_get_suffix_based_operators(self):
        self.assertEqual(get_query_operator("key1__lt", 10), "less")
        self.assertEqual(get_query_operator("key1__gte", 10), "greater_or_equal")
        self.assertEqual(get_query_operator("key1__within", 10), "range")



class RequestSendingTests(TestCase):

    @patch("requests.get")
    def test_successful_request(self, mock_get):
        mock_get.return_value.status_code = 200
        response = send_request('{"key": "value"}')
        mock_get.assert_called_with('https://search.rcsb.org/rcsbsearch/v2/query?json="{\\"key\\": \\"value\\"}"')
        self.assertIs(response, mock_get.return_value.json.return_value)
    

    @patch("requests.get")
    def test_unsuccessful_request(self, mock_get):
        mock_get.return_value.status_code = 500
        response = send_request('{"key": "value"}')
        mock_get.assert_called_with('https://search.rcsb.org/rcsbsearch/v2/query?json="{\\"key\\": \\"value\\"}"')
        self.assertIsNone(response)
