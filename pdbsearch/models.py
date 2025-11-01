from dataclasses import dataclass

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