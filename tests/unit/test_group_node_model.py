from unittest import TestCase
from unittest.mock import Mock
from pdbsearch.models import TerminalNode, GroupNode

class GroupNodeCreationTests(TestCase):

    def test_can_create_group_node(self):
        node = GroupNode(
            logical_operator="and",
            nodes=[1, 2])
        self.assertEqual(node.logical_operator, "and")
        self.assertEqual(node.nodes, [1, 2])



class GroupNodeSerializationTests(TestCase):

    def test_can_serialize_group_node(self):
        node1 = Mock(TerminalNode)
        node2 = Mock(TerminalNode)
        node = GroupNode(
            logical_operator="and",
            nodes=[node1, node2])
        self.assertEqual(node.serialize(), {
            "type": "group",
            "logical_operator": "and",
            "nodes": [node1.serialize.return_value, node2.serialize.return_value]
        })
        node1.serialize.assert_called_once()
        node2.serialize.assert_called_once()



class GroupNodeAndTests(TestCase):

    def test_and_with_terminal_node(self):
        node = GroupNode(logical_operator="and", nodes=[1, 2])
        other = Mock(TerminalNode)
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [1, 2, other])
    

    def test_or_with_terminal_node(self):
        node = GroupNode(logical_operator="or", nodes=[1, 2])
        other = Mock(TerminalNode)
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_and_with_and_group_node(self):
        node = GroupNode(logical_operator="and", nodes=[1, 2])
        other = Mock(GroupNode, logical_operator="and", nodes=[3, 4])
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [1, 2, 3, 4])
    

    def test_and_with_or_group_node(self):
        node = GroupNode(logical_operator="and", nodes=[1, 2])
        other = Mock(GroupNode, logical_operator="or", nodes=[3, 4])
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_or_with_and_group_node(self):
        node = GroupNode(logical_operator="or", nodes=[1, 2])
        other = Mock(GroupNode, logical_operator="and", nodes=[3, 4])
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_or_with_or_group_node(self):
        node = GroupNode(logical_operator="or", nodes=[1, 2])
        other = Mock(GroupNode, logical_operator="or", nodes=[3, 4])
        combined = node.and_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "and")
        self.assertEqual(combined.nodes, [node, other])



class GroupNodeOrTests(TestCase):

    def test_or_with_terminal_node(self):
        node = GroupNode(logical_operator="or", nodes=[1, 2])
        other = Mock(TerminalNode)
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [1, 2, other])
    

    def test_and_with_terminal_node(self):
        node = GroupNode(logical_operator="and", nodes=[1, 2])
        other = Mock(TerminalNode)
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_and_with_and_group_node(self):
        node = GroupNode(logical_operator="and", nodes=[1, 2])
        other = Mock(GroupNode, logical_operator="and", nodes=[3, 4])
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_and_with_or_group_node(self):
        node = GroupNode(logical_operator="and", nodes=[1, 2])
        other = Mock(GroupNode, logical_operator="or", nodes=[3, 4])
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_or_with_and_group_node(self):
        node = GroupNode(logical_operator="or", nodes=[1, 2])
        other = Mock(GroupNode, logical_operator="and", nodes=[3, 4])
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [node, other])
    

    def test_or_with_or_group_node(self):
        node = GroupNode(logical_operator="or", nodes=[1, 2])
        other = Mock(GroupNode, logical_operator="or", nodes=[3, 4])
        combined = node.or_(other)
        self.assertIsInstance(combined, GroupNode)
        self.assertEqual(combined.logical_operator, "or")
        self.assertEqual(combined.nodes, [1, 2, 3, 4])