from unittest import TestCase
from unittest.mock import patch
from pdbsearch.rcsb import *

class SearchTests(TestCase):

    @patch("pdbsearch.rcsb.apply_pagination")
    @patch("pdbsearch.rcsb.apply_sort")
    @patch("pdbsearch.rcsb.send_request")
    def test_successful_search(self, mock_req, mock_sort, mock_pag):
        mock_req.return_value = {"result_set": [
            {"identifier": "1XXX"}, {"identifier": "1YYY"}
        ]}
        result = search(start=10, limit=20, sort="xxx")
        mock_pag.assert_called_with({
            "return_type": "entry", "query": {"type": "terminal", "service": "text"}
        }, 10, 20)
        mock_sort.assert_called_with({
            "return_type": "entry", "query": {"type": "terminal", "service": "text"}
        }, "xxx")
        mock_req.assert_called_with({
            "return_type": "entry", "query": {"type": "terminal", "service": "text"}
        })
        self.assertEqual(result, ["1XXX", "1YYY"])
    

    @patch("pdbsearch.rcsb.apply_pagination")
    @patch("pdbsearch.rcsb.apply_sort")
    @patch("pdbsearch.rcsb.send_request")
    def test_unsuccessful_search(self, mock_req, mock_sort, mock_pag):
        mock_req.return_value = None
        result = search(start=10, limit=20, sort="xxx")
        mock_pag.assert_called_with({
            "return_type": "entry", "query": {"type": "terminal", "service": "text"}
        }, 10, 20)
        mock_sort.assert_called_with({
            "return_type": "entry", "query": {"type": "terminal", "service": "text"}
        }, "xxx")
        mock_req.assert_called_with({
            "return_type": "entry", "query": {"type": "terminal", "service": "text"}
        })
        self.assertIsNone(result)




class PaginationApplyingTests(TestCase):

    def test_can_get_all_codes(self):
        query = {}
        apply_pagination(query, 0, None)
        self.assertEqual(query, {"request_options": {"return_all_hits": True}})
    

    def test_can_get_limit_codes(self):
        query = {}
        apply_pagination(query, 10, 45)
        self.assertEqual(query, {"request_options": {"pager": {"start": 10, "rows": 45}}})


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


class RequestSendingTests(TestCase):

    @patch("requests.get")
    def test_successful_request(self, mock_get):
        mock_get.return_value.status_code = 200
        response = send_request('{"key": "value"}')
        mock_get.assert_called_with('https://search.rcsb.org/rcsbsearch/v1/query?json="{\\"key\\": \\"value\\"}"')
        self.assertIs(response, mock_get.return_value.json.return_value)
    

    @patch("requests.get")
    def test_unsuccessful_request(self, mock_get):
        mock_get.return_value.status_code = 500
        response = send_request('{"key": "value"}')
        mock_get.assert_called_with('https://search.rcsb.org/rcsbsearch/v1/query?json="{\\"key\\": \\"value\\"}"')
        self.assertIsNone(response)
