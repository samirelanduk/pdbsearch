from unittest import TestCase
from pdbsearch.models import TerminalNode

class TerminalNodeCreationTests(TestCase):

    def test_can_create_terminal_node(self):
        node = TerminalNode("service", {"key": "value"})
        self.assertEqual(node.service, "service")
        self.assertEqual(node.parameters, {"key": "value"})