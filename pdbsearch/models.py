from dataclasses import dataclass
from .request import send_request, create_request_options

@dataclass
class TerminalNode:
    """A terminal node in a query graph. It specifies one search criterion.
    
    :param str service: the name of the RCSB search service to use.
    :param dict parameters: the parameters for the search."""

    service: str
    parameters: dict

    def serialize(self):
        """Returns a JSON-serializable representation of the node.
        
        :rtype: ``dict``"""

        node = {"type": "terminal", "service": self.service}
        if self.parameters: node["parameters"] = self.parameters
        return node
    

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
class GroupNode:
    """A group node in a query graph. It combines multiple nodes with a logical
    operator for arbitrary boolean logic.

    :param str logical_operator: the logical operator to use for the group.
    :param list nodes: the nodes to group."""

    logical_operator: str
    nodes: list

    def serialize(self):
        """Returns a JSON-serializable representation of the node.
        
        :rtype: ``dict``"""

        return {
            "type": "group",
            "logical_operator": self.logical_operator,
            "nodes": [node.serialize() for node in self.nodes]
        }