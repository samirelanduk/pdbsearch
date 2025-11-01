from unittest import TestCase
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