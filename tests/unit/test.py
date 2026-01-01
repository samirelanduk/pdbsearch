from unittest import TestCase
from unittest.mock import patch, Mock
from pdbsearch import full_text_node, search, send_request, create_request_options, SEARCH_URL

class FullTextNodeTests(TestCase):

    def test_can_create_full_text_node(self):
        node = full_text_node("thymidine kinase")
        self.assertEqual(node.service, "full_text")
        self.assertEqual(node.parameters, {"value": "thymidine kinase"})



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