from dataclasses import dataclass
from .request import send_request

@dataclass
class TerminalNode:
    """A terminal node in a query graph. It specifies one search criterion.
    
    :param str service: the name of the RCSB search service to use.
    :param dict parameters: the parameters for the search."""

    service: str
    parameters: dict

    def serialize(self):
        """Returns a JSON-serializable representation of the node."""

        node = {"type": "terminal", "service": self.service}
        if self.parameters: node["parameters"] = self.parameters
        return node
    

    def execute(self, return_type, ids_only=False):
        """Executes the node and returns the result.
        
        :param str return_type: the RCSB object type to search for.
        :param bool ids_only: whether to return only the result identifiers.
        :rtype: ``list`` or ``dict``"""

        request = {"return_type": return_type, "query": self.serialize()}
        return send_request(request, ids_only=ids_only)