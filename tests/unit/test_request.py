from unittest import TestCase
from unittest.mock import patch
from pdbsearch.request import send_request, SEARCH_URL, create_request_options

class SendRequestTests(TestCase):

    def setUp(self):
        self.patch1 = patch("pdbsearch.request.requests.post")
        self.mock_post = self.patch1.start()
        self.mock_post.return_value.status_code = 200
        self.mock_post.return_value.json.return_value = {"result_set": [{"identifier": 1}, {"identifier": 2}, {"identifier": 3}]}
    

    def tearDown(self):
        self.patch1.stop()
    

    def test_can_send_request(self):
        result = send_request({1: 2})
        self.mock_post.assert_called_once_with(SEARCH_URL, json={1: 2})
        self.assertEqual(result, {"result_set": [{"identifier": 1}, {"identifier": 2}, {"identifier": 3}]})
    

    def test_can_send_request_with_ids_only(self):
        result = send_request({1: 2}, ids_only=True)
        self.mock_post.assert_called_once_with(SEARCH_URL, json={1: 2})
        self.assertEqual(result, [1, 2, 3])
    

    def test_can_send_request_with_none_response(self):
        self.mock_post.return_value.status_code = 204
        result = send_request({1: 2})
        self.mock_post.assert_called_once_with(SEARCH_URL, json={1: 2})
        self.assertIsNone(result)



class CreateRequestOptionsTests(TestCase):

    def test_no_options(self):
        result = create_request_options()
        self.assertIsNone(result)
    

    def test_return_all(self):
        result = create_request_options(return_all=True)
        self.assertEqual(result, {"return_all_hits": True})
    

    def test_counts_only(self):
        result = create_request_options(counts_only=True)
        self.assertEqual(result, {"return_counts": True})
    

    def test_start_and_rows(self):
        result = create_request_options(start=10, rows=20)
        self.assertEqual(result, {"paginate": {"start": 10, "rows": 20}})