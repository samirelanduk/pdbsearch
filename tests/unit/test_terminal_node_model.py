from unittest import TestCase
from pdbsearch import TerminalNode

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