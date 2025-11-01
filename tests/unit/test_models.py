from unittest import TestCase
from unittest.mock import patch
from pdbsearch.models import TerminalNode

class TerminalNodeCreationTests(TestCase):

    def test_can_create_terminal_node(self):
        node = TerminalNode("service_name", {"key": "value"})
        self.assertEqual(node.service, "service_name")
        self.assertEqual(node.parameters, {"key": "value"})



class TerminalNodeSerializationTests(TestCase):

    def test_can_serialize_without_parameters(self):
        node = TerminalNode(service="service_name", parameters=None)
        self.assertEqual(node.serialize(), {"type": "terminal", "service": "service_name"})


    def test_can_serialize_with_parameters(self):
        node = TerminalNode(service="service_name", parameters={"key": "value"})
        self.assertEqual(node.serialize(), {"type": "terminal", "service": "service_name", "parameters": {"key": "value"}})



class TerminalNodeExecutionTests(TestCase):

    @patch("pdbsearch.models.TerminalNode.serialize")
    @patch("pdbsearch.models.send_request")
    def test_can_execute_terminal_node(self, mock_send_request, mock_serialize):
        node = TerminalNode(service="service_name", parameters={"key": "value"})
        result = node.execute(return_type="entry")
        self.assertEqual(result, mock_send_request.return_value)
        mock_send_request.assert_called_once_with(
            {"return_type": "entry", "query": mock_serialize.return_value},
            ids_only=False
        )
        mock_serialize.assert_called_once_with()
    

    @patch("pdbsearch.models.TerminalNode.serialize")
    @patch("pdbsearch.models.send_request")
    def test_can_execute_terminal_node_ids_only(self, mock_send_request, mock_serialize):
        node = TerminalNode(service="service_name", parameters={"key": "value"})
        result = node.execute(return_type="entry", ids_only=True)
        self.assertEqual(result, mock_send_request.return_value)
        mock_send_request.assert_called_once_with(
            {"return_type": "entry", "query": mock_serialize.return_value},
            ids_only=True
        )
        mock_serialize.assert_called_once_with()
