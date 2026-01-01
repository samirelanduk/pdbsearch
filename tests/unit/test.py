from unittest import TestCase
from unittest.mock import patch
from pdbsearch import search, send_request, SEARCH_URL

class SearchTests(TestCase):

    @patch("pdbsearch.send_request")
    def test_can_search(self, mock_send_request):
        result = search("entry")
        mock_send_request.assert_called_once_with({"return_type": "entry"})
        self.assertEqual(result, mock_send_request.return_value)



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