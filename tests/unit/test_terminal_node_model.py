from unittest import TestCase
from unittest.mock import Mock, patch
from pdbsearch.models import TerminalNode, GroupNode

class TerminalNodeCreationTests(TestCase):

    def test_can_create_terminal_node(self):
        node = TerminalNode(
            service="text", 
            parameters={1: 2})
        self.assertEqual(node.service, "text")
        self.assertEqual(node.parameters, {1: 2})



class TerminalNodeSerializationTests(TestCase):

    def test_can_serialize_terminal_node(self):
        node = TerminalNode(
            service="text", 
            parameters={1: 2})
        self.assertEqual(node.serialize(), {"type": "terminal", "service": "text", "parameters": {1: 2}})



class TerminalNodeAndTests(TestCase):

    def test_other_terminal_node(self):
        other = Mock(TerminalNode)
        node = TerminalNode("text", {"key": "value"})
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_and_group_node(self):
        other = Mock(GroupNode, logical_operator="and", nodes=[1, 2])
        node = TerminalNode("text", {"key": "value"})
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, 1, 2])
    

    def test_or_group_node(self):
        other = Mock(GroupNode, logical_operator="or", nodes=[1, 2])
        node = TerminalNode("text", {"key": "value"})
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])



class TerminalNodeOrTests(TestCase):

    def test_other_terminal_node(self):
        other = Mock(TerminalNode)
        node = TerminalNode("text", {"key": "value"})
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_or_group_node(self):
        other = Mock(GroupNode, logical_operator="or", nodes=[1, 2])
        node = TerminalNode("text", {"key": "value"})
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, 1, 2])
    

    def test_and_group_node(self):
        other = Mock(GroupNode, logical_operator="and", nodes=[1, 2])
        node = TerminalNode("text", {"key": "value"})
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])



# Base class method, tested here rather than in the GroupNodeTests class
class TerminalNodeSearchTests(TestCase):

    @patch("pdbsearch.models.search")
    def test_can_search(self, mock_search):
        node = TerminalNode("text", {"key": "value"})
        node.search("entry")
        mock_search.assert_called_once_with("entry", node, False, None, None)
    

    @patch("pdbsearch.models.search")
    def test_can_search_with_options(self, mock_search):
        node = TerminalNode("text", {"key": "value"})
        node.search("entry", return_all=True, start=10, rows=20)
        mock_search.assert_called_once_with("entry", node, True, 10, 20)