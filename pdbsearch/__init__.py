import requests
from dataclasses import dataclass

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

@dataclass
class TerminalNode:
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



def search(return_type, node=None, return_all=False, start=None, rows=None):
    """Queries the RCSB search API.

    :param str return_type: the type of data to return.
    :param bool return_all: whether to return all results, unpaginated.
    :rtype: ``dict``"""

    query = {
        "return_type": return_type,
    }
    if node: query["query"] = node.serialize()
    if request_options := create_request_options(return_all, start, rows):
        query["request_options"] = request_options
    return send_request(query)


def create_request_options(return_all=False, start=None, rows=None):
    """Creates a request options dictionary for the RCSB search API.
    
    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :rtype: ``dict``"""

    request_options = {}
    if return_all:
        request_options["return_all_hits"] = True
    if (start is not None) or (rows is not None):
        request_options["paginate"] = {}
        if start is not None:
            request_options["paginate"]["start"] = start
        if rows is not None:
            request_options["paginate"]["rows"] = rows
    return request_options


def send_request(query):
    """Sends a query dictionary to the RCSB search API. If a valid response is
    received, this will be returned in JSON format. Otherwise ``None`` will be
    returned.
    
    :param dict query: the query, formatted to RCSB specifications.
    :rtype: ``dict``"""

    response = requests.post(SEARCH_URL, json=query)
    if response.status_code == 200:
        return response.json()