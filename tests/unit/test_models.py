from unittest import TestCase
from unittest.mock import patch, Mock
from pdbsearch.models import TerminalNode, GroupNode

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
    @patch("pdbsearch.models.create_request_options")
    @patch("pdbsearch.models.send_request")
    def test_can_execute_terminal_node(self, mock_send_request, mock_create_request_options, mock_serialize):
        mock_create_request_options.return_value = None
        node = TerminalNode(service="service_name", parameters={"key": "value"})
        result = node.execute(return_type="entry")
        self.assertEqual(result, mock_send_request.return_value)
        mock_send_request.assert_called_once_with(
            {"return_type": "entry", "query": mock_serialize.return_value},
            ids_only=False
        )
        mock_serialize.assert_called_once_with()
    

    @patch("pdbsearch.models.TerminalNode.serialize")
    @patch("pdbsearch.models.create_request_options")
    @patch("pdbsearch.models.send_request")
    def test_can_execute_terminal_node_ids_only(self, mock_send_request, mock_create_request_options, mock_serialize):
        mock_create_request_options.return_value = None
        node = TerminalNode(service="service_name", parameters={"key": "value"})
        result = node.execute(return_type="entry", ids_only=True)
        self.assertEqual(result, mock_send_request.return_value)
        mock_send_request.assert_called_once_with(
            {"return_type": "entry", "query": mock_serialize.return_value},
            ids_only=True
        )
        mock_serialize.assert_called_once_with()
    

    @patch("pdbsearch.models.TerminalNode.serialize")
    @patch("pdbsearch.models.create_request_options")
    @patch("pdbsearch.models.send_request")
    def test_can_execute_terminal_node_with_request_options(self, mock_send_request, mock_create_request_options, mock_serialize):
        mock_create_request_options.return_value = {"paginate": "sure"}
        node = TerminalNode(service="service_name", parameters={"key": "value"})
        result = node.execute(return_type="entry", return_all=True, start=10, rows=20, counts_only=True)
        self.assertEqual(result, mock_send_request.return_value)
        mock_send_request.assert_called_once_with(
            {"return_type": "entry", "query": mock_serialize.return_value, "request_options": {"paginate": "sure"}},
            ids_only=False)
        mock_serialize.assert_called_once_with()
        mock_create_request_options.assert_called_once_with(
            return_all=True,
            start=10,
            rows=20,
            counts_only=True
        )



class GroupNodeCreationTests(TestCase):

    def test_can_create_group_node(self):
        node = GroupNode("and", [1, 2])
        self.assertEqual(node.logical_operator, "and")
        self.assertEqual(node.nodes, [1, 2])



class GroupNodeSerializationTests(TestCase):

    def test_can_serialize_group_node(self):
        node1, node2 = Mock(), Mock()
        node = GroupNode("and", [node1, node2])
        self.assertEqual(node.serialize(), {
            "type": "group",
            "logical_operator": "and",
            "nodes": [node1.serialize.return_value, node2.serialize.return_value]
        })
        node1.serialize.assert_called_once_with()
        node2.serialize.assert_called_once_with()