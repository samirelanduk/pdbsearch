from unittest import TestCase
from pdbsearch.models import TerminalNode

class TerminalNodeCreationTests(TestCase):

    def test_can_create_terminal_node(self):
        node = TerminalNode("service_name", {"key": "value"})
        self.assertEqual(node.service, "service_name")
        self.assertEqual(node.parameters, {"key": "value"})