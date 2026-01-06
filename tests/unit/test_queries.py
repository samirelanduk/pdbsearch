import io
import sys
import requests
from unittest import TestCase
from unittest.mock import patch, Mock
from pdbsearch.queries import query, send_request, create_request_options, SEARCH_URL

class QueryTests(TestCase):

    @patch("pdbsearch.queries.create_request_options")
    @patch("pdbsearch.queries.send_request")
    def test_minimal_search(self, mock_send_request, mock_create_request_options):
        mock_create_request_options.return_value = {}
        result = query("entry")
        mock_send_request.assert_called_once_with({"return_type": "entry"})
        self.assertEqual(result, mock_send_request.return_value)


    @patch("pdbsearch.queries.create_request_options")
    @patch("pdbsearch.queries.send_request")
    def test_can_search_with_node(self, mock_send_request, mock_create_request_options):
        mock_create_request_options.return_value = {}
        node = Mock()
        result = query("entry", node=node)
        mock_send_request.assert_called_once_with({"return_type": "entry", "query": node.serialize.return_value})
        self.assertEqual(result, mock_send_request.return_value)
    

    @patch("pdbsearch.queries.create_request_options")
    @patch("pdbsearch.queries.send_request")
    def test_can_search_with_options(self, mock_send_request, mock_create_request_options):
        mock_create_request_options.return_value = {"xxx": True}
        result = query("entry", return_all=True)
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
    

    def test_single_sort_attribute(self):
        result = create_request_options(sort="rcsb_accession_info.initial_release_date")
        self.assertEqual(result, {"sort": [{"sort_by": "rcsb_accession_info.initial_release_date", "direction": "asc"}]})
    

    def test_reverse_sort_attribute(self):
        result = create_request_options(sort="-rcsb_accession_info.initial_release_date")
        self.assertEqual(result, {"sort": [{"sort_by": "rcsb_accession_info.initial_release_date", "direction": "desc"}]})
    

    def test_multiple_sort_attributes(self):
        result = create_request_options(sort=["-rcsb_accession_info.initial_release_date", "rcsb_accession_info__deposit_date"])
        self.assertEqual(result, {"sort": [
            {"sort_by": "rcsb_accession_info.initial_release_date", "direction": "desc"},
            {"sort_by": "rcsb_accession_info.deposit_date", "direction": "asc"}
        ]})



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
    

    def test_can_handle_204_response(self):
        self.mock_post.return_value.status_code = 204
        result = send_request({1: 2})
        self.mock_post.assert_called_once_with(SEARCH_URL, json={1: 2})
        self.assertEqual(result, None)
        stderr_output = self.stderr.getvalue()
        self.assertEqual(stderr_output, "")


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