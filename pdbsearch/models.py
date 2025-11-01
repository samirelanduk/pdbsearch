from dataclasses import dataclass
from .request import send_request, create_request_options
from .query import query
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


    def execute(self, return_type, return_all=False, start=None, rows=None, counts_only=False, ids_only=False):
        """Executes the node and returns the result.
        
        :param str return_type: the RCSB object type to search for.
        :param bool return_all: whether to return all hits rather than paginating.
        :param int start: the start index for pagination.
        :param int rows: the page size.
        :param bool counts_only: whether to return only the results count.
        :param bool ids_only: whether to return only the result identifiers.
        :rtype: ``list`` or ``dict``"""

        request = {"return_type": return_type, "query": self.serialize()}
        if request_options := create_request_options(
            return_all=return_all,
            start=start,
            rows=rows,
            counts_only=counts_only
        ):
            request["request_options"] = request_options
        return send_request(request, ids_only=ids_only)



@dataclass
class TerminalNode(QueryNode):
    """A terminal node in a query graph. It specifies one search criterion.
    
    :param str service: the name of the RCSB search service to use.
    :param dict parameters: the parameters for the search."""

    service: str
    parameters: dict

    def and_(self, *args, **kwargs):
        """Combines this terminal node with another node using the AND logical
        operator, to create a new group node.

        You can either provide another node as a single positional argument, or
        you can provide keyword arguments to the query function.
        
        :rtype: ``GroupNode``"""

        if len(args) == 1 and isinstance(args[0], QueryNode):
            other = args[0]
        else:
            other = query(*args, **kwargs)
        if isinstance(other, GroupNode) and other.logical_operator == "and":
            return GroupNode("and", [self, *other.nodes])
        return GroupNode("and", [self, other])
    

    def or_(self, *args, **kwargs):
        """Combines this terminal node with another node using the OR logical
        operator, to create a new group node.

        You can either provide another node as a single positional argument, or
        you can provide keyword arguments to the query function.
        
        :rtype: ``GroupNode``"""

        if len(args) == 1 and isinstance(args[0], QueryNode):
            other = args[0]
        else:
            other = query(*args, **kwargs)
        if isinstance(other, GroupNode) and other.logical_operator == "or":
            return GroupNode("or", [self, *other.nodes])
        return GroupNode("or", [self, other])


    def serialize(self):
        """Returns a JSON-serializable representation of the node.
        
        :rtype: ``dict``"""

        node = {"type": "terminal", "service": self.service}
        if self.parameters: node["parameters"] = self.parameters
        return node



@dataclass
class GroupNode(QueryNode):
    """A group node in a query graph. It combines multiple nodes with a logical
    operator for arbitrary boolean logic.

    :param str logical_operator: the logical operator to use for the group.
    :param list nodes: the nodes to group."""

    logical_operator: str
    nodes: list[QueryNode]

    def and_(self, *args, **kwargs):
        """Combines this group node with another node using the AND logical
        operator, to create a new group node.

        You can either provide another node as a single positional argument, or
        you can provide keyword arguments to the query function.
        
        :rtype: ``GroupNode``"""

        if len(args) == 1 and isinstance(args[0], QueryNode):
            other = args[0]
        else:
            other = query(*args, **kwargs)
        if isinstance(other, TerminalNode):
            if self.logical_operator == "and":
                return GroupNode("and", [*self.nodes, other])
            elif self.logical_operator == "or":
                return GroupNode("and", [self, other])
        elif self.logical_operator == other.logical_operator == "and":
            return GroupNode("and", [*self.nodes, *other.nodes])
        return GroupNode("and", [self, other])


    def or_(self, *args, **kwargs):
        """Combines this group node with another node using the OR logical
        operator, to create a new group node.

        You can either provide another node as a single positional argument, or
        you can provide keyword arguments to the query function.
        
        :rtype: ``GroupNode``"""

        if len(args) == 1 and isinstance(args[0], QueryNode):
            other = args[0]
        else:
            other = query(*args, **kwargs)
        if isinstance(other, TerminalNode):
            if self.logical_operator == "and":
                return GroupNode("or", [self, other])
            elif self.logical_operator == "or":
                return GroupNode("or", [*self.nodes, other])
        elif self.logical_operator == other.logical_operator == "or":
            return GroupNode("or", [*self.nodes, *other.nodes])
        return GroupNode("or", [self, other])
    

    def serialize(self):
        """Returns a JSON-serializable representation of the node.
        
        :rtype: ``dict``"""

        return {
            "type": "group",
            "logical_operator": self.logical_operator,
            "nodes": [node.serialize() for node in self.nodes]
        }