from unittest import TestCase
from unittest.mock import patch
from pdbsearch.rcsb import *

class SearchTests(TestCase):

    def setUp(self):
        self.patch1 = patch("requests.get")
        self.mock_get = self.patch1.start()
        self.mock_get.return_value.status_code = 200
        self.mock_get.return_value.json.return_value = {
            "result_set": [{"identifier": "1ABC"}, {"identifier": "2ABC"}]
        }
    

    def tearDown(self):
        self.patch1.stop()


    def test_default_search(self):
        self.assertEqual(search(), ["1ABC", "2ABC"])
        query = {
            "return_type": "entry",
            "query": {"type": "terminal", "service": "text"},
            "request_options": {"pager": {"start": 0, "rows": 10}}
        }
        self.mock_get.assert_called_with(f"{SEARCH_URL}{json.dumps(query)}")
    

    def test_test_can_set_start(self):
        self.assertEqual(search(start=3), ["1ABC", "2ABC"])
        query = {
            "return_type": "entry",
            "query": {"type": "terminal", "service": "text"},
            "request_options": {"pager": {"start": 3, "rows": 10}}
        }
        self.mock_get.assert_called_with(f"{SEARCH_URL}{json.dumps(query)}")
    

    def test_test_can_set_limit(self):
        self.assertEqual(search(limit=12), ["1ABC", "2ABC"])
        query = {
            "return_type": "entry",
            "query": {"type": "terminal", "service": "text"},
            "request_options": {"pager": {"start": 0, "rows": 12}}
        }
        self.mock_get.assert_called_with(f"{SEARCH_URL}{json.dumps(query)}")
    

    def test_test_can_set_no_limit(self):
        self.assertEqual(search(limit=None), ["1ABC", "2ABC"])
        query = {
            "return_type": "entry",
            "query": {"type": "terminal", "service": "text"},
            "request_options": {"return_all_hits": True}
        }
        self.mock_get.assert_called_with(f"{SEARCH_URL}{json.dumps(query)}")
