from unittest import TestCase
from unittest.mock import patch, Mock
from pdbsearch.models import TerminalNode, GroupNode, QueryNode

class QueryNodeExecutionTests(TestCase):

    def setUp(self):
        class SubNode(QueryNode):
            def serialize(self):
                return {"type": "sub", "value": "value"}
            def and_(self):
                pass
            def or_(self):
                pass
        self.SubNode = SubNode


    @patch("pdbsearch.models.create_request_options")
    @patch("pdbsearch.models.send_request")
    def test_can_execute_node(self, mock_send_request, mock_create_request_options):
        mock_create_request_options.return_value = None
        node = self.SubNode()
        result = node.execute(return_type="entry")
        self.assertEqual(result, mock_send_request.return_value)
        mock_send_request.assert_called_once_with(
            {"return_type": "entry", "query": {"type": "sub", "value": "value"}},
            ids_only=False
        )
    

    @patch("pdbsearch.models.create_request_options")
    @patch("pdbsearch.models.send_request")
    def test_can_execute_terminal_node_ids_only(self, mock_send_request, mock_create_request_options):
        mock_create_request_options.return_value = None
        node = self.SubNode()
        result = node.execute(return_type="entry", ids_only=True)
        self.assertEqual(result, mock_send_request.return_value)
        mock_send_request.assert_called_once_with(
            {"return_type": "entry", "query": {"type": "sub", "value": "value"}},
            ids_only=True
        )
    

    @patch("pdbsearch.models.create_request_options")
    @patch("pdbsearch.models.send_request")
    def test_can_execute_terminal_node_with_request_options(self, mock_send_request, mock_create_request_options):
        mock_create_request_options.return_value = {"paginate": "sure"}
        node = self.SubNode()
        result = node.execute(return_type="entry", return_all=True, start=10, rows=20, counts_only=True)
        self.assertEqual(result, mock_send_request.return_value)
        mock_send_request.assert_called_once_with(
            {"return_type": "entry", "query": {"type": "sub", "value": "value"}, "request_options": {"paginate": "sure"}},
            ids_only=False)
        mock_create_request_options.assert_called_once_with(
            return_all=True,
            start=10,
            rows=20,
            counts_only=True
        )



class TerminalNodeCreationTests(TestCase):

    def test_can_create_terminal_node(self):
        node = TerminalNode("service_name", {"key": "value"})
        self.assertEqual(node.service, "service_name")
        self.assertEqual(node.parameters, {"key": "value"})



class TerminalNodeAndTests(TestCase):

    @patch("pdbsearch.models.query")
    def test_can_and_with_params(self, mock_query):
        mock_query.return_value = "query"
        node = TerminalNode("text", {"key": "value"})
        combined = node.and_(a=1, b=2)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, "query"])
        mock_query.assert_called_once_with(a=1, b=2)
    

    def test_can_and_with_terminal_node(self):
        other = Mock(TerminalNode)
        node = TerminalNode("text", {"key": "value"})
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_can_and_with_and_group_node(self):
        other = Mock(GroupNode, logical_operator="and", nodes=[1, 2])
        node = TerminalNode("text", {"key": "value"})
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, 1, 2])
    

    def test_can_and_with_or_group_node(self):
        other = Mock(GroupNode, logical_operator="or", nodes=[1, 2])
        node = TerminalNode("text", {"key": "value"})
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])



class TerminalNodeOrTests(TestCase):

    @patch("pdbsearch.models.query")
    def test_can_or_with_params(self, mock_query):
        mock_query.return_value = "query"
        node = TerminalNode("text", {"key": "value"})
        combined = node.or_(a=1, b=2)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, "query"])
        mock_query.assert_called_once_with(a=1, b=2)
    

    def test_can_or_with_terminal_node(self):
        other = Mock(TerminalNode)
        node = TerminalNode("text", {"key": "value"})
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_can_or_with_and_group_node(self):
        other = Mock(GroupNode, logical_operator="and", nodes=[1, 2])
        node = TerminalNode("text", {"key": "value"})
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_can_or_with_or_group_node(self):
        other = Mock(GroupNode, logical_operator="or", nodes=[1, 2])
        node = TerminalNode("text", {"key": "value"})
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, 1, 2])



class TerminalNodeSerializationTests(TestCase):

    def test_can_serialize_without_parameters(self):
        node = TerminalNode(service="service_name", parameters=None)
        self.assertEqual(node.serialize(), {"type": "terminal", "service": "service_name"})


    def test_can_serialize_with_parameters(self):
        node = TerminalNode(service="service_name", parameters={"key": "value"})
        self.assertEqual(node.serialize(), {"type": "terminal", "service": "service_name", "parameters": {"key": "value"}})



class GroupNodeCreationTests(TestCase):

    def test_can_create_group_node(self):
        node = GroupNode("and", [1, 2])
        self.assertEqual(node.logical_operator, "and")
        self.assertEqual(node.nodes, [1, 2])



class GroupNodeAndTests(TestCase):

    @patch("pdbsearch.models.query")
    def test_can_and_with_params_as_and_node(self, mock_query):
        mock_query.return_value = Mock(TerminalNode)
        node = GroupNode("and", [1, 2])
        combined = node.and_(a=1, b=2)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [1, 2, mock_query.return_value])
        mock_query.assert_called_once_with(a=1, b=2)
    

    @patch("pdbsearch.models.query")
    def test_can_and_with_params_as_or_node(self, mock_query):
        mock_query.return_value = Mock(TerminalNode)
        node = GroupNode("or", [1, 2])
        combined = node.and_(a=1, b=2)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, mock_query.return_value])
        mock_query.assert_called_once_with(a=1, b=2)
    

    def test_can_and_with_terminal_node_as_and_node(self):
        other = Mock(TerminalNode)
        node = GroupNode("and", [1, 2])
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [1, 2, other])
    

    def test_can_and_with_terminal_node_as_or_node(self):
        other = Mock(TerminalNode)
        node = GroupNode("or", [1, 2])
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_can_and_with_and_group_node_as_and_node(self):
        other = Mock(GroupNode, logical_operator="and", nodes=[1, 2])
        node = GroupNode("and", [3, 4])
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [3, 4, 1, 2])
    

    def test_can_and_with_and_group_node_as_or_node(self):
        other = Mock(GroupNode, logical_operator="and", nodes=[1, 2])
        node = GroupNode("or", [3, 4])
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_can_and_with_or_group_node_as_and_node(self):
        other = Mock(GroupNode, logical_operator="or", nodes=[1, 2])
        node = GroupNode("and", [3, 4])
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])

    
    def test_can_and_with_or_group_node_as_or_node(self):
        other = Mock(GroupNode, logical_operator="or", nodes=[1, 2])
        node = GroupNode("or", [3, 4])
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])



class GroupNodeOrTests(TestCase):

    @patch("pdbsearch.models.query")
    def test_can_or_with_params_as_and_node(self, mock_query):
        mock_query.return_value = Mock(TerminalNode)
        node = GroupNode("and", [1, 2])
        combined = node.or_(a=1, b=2)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, mock_query.return_value])
        mock_query.assert_called_once_with(a=1, b=2)
    

    @patch("pdbsearch.models.query")
    def test_can_or_with_params_as_or_node(self, mock_query):
        mock_query.return_value = Mock(TerminalNode)
        node = GroupNode("or", [1, 2])
        combined = node.or_(a=1, b=2)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [1, 2, mock_query.return_value])
        mock_query.assert_called_once_with(a=1, b=2)
    

    def test_can_or_with_terminal_node_as_and_node(self):
        other = Mock(TerminalNode)
        node = GroupNode("and", [1, 2])
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])
    
    
    def test_can_or_with_terminal_node_as_or_node(self):
        other = Mock(TerminalNode)
        node = GroupNode("or", [1, 2])
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [1, 2, other])
    

    def test_can_or_with_and_group_node_as_and_node(self):
        other = Mock(GroupNode, logical_operator="and", nodes=[1, 2])
        node = GroupNode("and", [3, 4])
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])

    
    def test_can_or_with_and_group_node_as_or_node(self):
        other = Mock(GroupNode, logical_operator="and", nodes=[1, 2])
        node = GroupNode("or", [3, 4])
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_can_or_with_or_group_node_as_and_node(self):
        other = Mock(GroupNode, logical_operator="or", nodes=[1, 2])
        node = GroupNode("and", [3, 4])
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_can_or_with_or_group_node_as_or_node(self):
        other = Mock(GroupNode, logical_operator="or", nodes=[1, 2])
        node = GroupNode("or", [3, 4])
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [3, 4, 1, 2])
    


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