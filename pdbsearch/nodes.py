from dataclasses import dataclass
from abc import ABC, abstractmethod

class QueryNode(ABC):
    """A base class for all query nodes."""

    @abstractmethod
    def serialize(self):
        pass

    
    @abstractmethod
    def and_(self, *args, **kwargs):
        pass


    @abstractmethod
    def or_(self, *args, **kwargs):
        pass



@dataclass
class TerminalNode(QueryNode):
    """A terminal node in a query graph, which represents a single search term.

    :param str service: the service to use for the terminal node.
    :param dict parameters: the parameters to use for the terminal node."""

    service: str
    parameters: dict

    def serialize(self):
        """Creates the JSON-serializable representation of the node.
        
        :rtype: ``dict``"""

        return {
            "type": "terminal",
            "service": self.service,
            "parameters": self.parameters
        }
    

    def and_(self, node):
        """Combines this terminal node with another node using the AND logical
        operator, to create a new group node.
        
        :rtype: ``GroupNode``"""

        if isinstance(node, GroupNode) and node.logical_operator == "and":
            return GroupNode("and", [self, *node.nodes])
        return GroupNode("and", [self, node])
    

    def or_(self, node):
        """Combines this terminal node with another node using the OR logical
        operator, to create a new group node.
        
        :rtype: ``GroupNode``"""

        if isinstance(node, GroupNode) and node.logical_operator == "or":
            return GroupNode("or", [self, *node.nodes])
        return GroupNode("or", [self, node])



@dataclass
class GroupNode:
    """A group node in a query graph, which combines other nodes with boolean
    logic.

    :param str logical_operator: the logical operator to use for the group node.
    :param list[TerminalNode] nodes: the nodes to combine."""

    logical_operator: str
    nodes: list[TerminalNode]

    def serialize(self):
        """Returns a JSON-serializable representation of the node.
        
        :rtype: ``dict``"""

        return {
            "type": "group",
            "logical_operator": self.logical_operator,
            "nodes": [node.serialize() for node in self.nodes]
        }
    

    def and_(self, node):
        """Combines this group node with another node using the AND logical
        operator, to create a new group node.
        
        :rtype: ``GroupNode``"""

        if isinstance(node, TerminalNode):
            if self.logical_operator == "and":
                return GroupNode("and", [*self.nodes, node])
            elif self.logical_operator == "or":
                return GroupNode("and", [self, node])
        elif self.logical_operator == node.logical_operator == "and":
            return GroupNode("and", [*self.nodes, *node.nodes])
        return GroupNode("and", [self, node])
    

    def or_(self, node):
        """Combines this group node with another node using the OR logical
        operator, to create a new group node.
        
        :rtype: ``GroupNode``"""

        if isinstance(node, TerminalNode):
            if self.logical_operator == "and":
                return GroupNode("or", [self, node])
            elif self.logical_operator == "or":
                return GroupNode("or", [*self.nodes, node])
        elif self.logical_operator == node.logical_operator == "or":
            return GroupNode("or", [*self.nodes, *node.nodes])
        return GroupNode("or", [self, node])