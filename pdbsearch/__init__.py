import requests
from dataclasses import dataclass
from pdbsearch.terms import TEXT_TERMS

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


def full_text_node(term):
    """Creates a full text node for some search term.
    
    :param str term: the search term.
    :rtype: ``TerminalNode``"""

    return TerminalNode(
        service="full_text", 
        parameters={"value": term}
    )


def text_node(**kwargs):
    """Creates a text node for some search term. Only one key=value pair can be
    provided, and it must correspond to a valid term in the schema.

    :param kwargs: the key=value pairs to create the node from.
    :rtype: ``TerminalNode``"""

    if not kwargs: raise ValueError("At least one keyword argument is required")
    if len(kwargs) > 1: raise ValueError("Only one keyword argument is allowed")
    key, value = next(iter(kwargs.items()))
    parameters = get_text_parameters(key, value)
    return TerminalNode(
        service="text", 
        parameters=parameters
    )


def get_text_parameters(key, value):
    """Generates the parameters dictionary for a text search, using the
    key=value passed to the ``text_node`` function. It will parse the suffixes
    to determine the operator and negation.

    These are the suffixes that produce the corresponding operators (to
    determine whether to use ``equals`` or ``exact_match``, we check the schema
    to see if the term is numeric):

    .. code-block:: text
    
        __gt                greater_than
        __lt                less_than
        __gte               greater_or_equal
        __lte               less_or_equal
        __in                in
        __exists            exists
        __range             range
        __contains          contains_phrase
        __contains_phrase   contains_phrase
        __contains_words    contains_words
                            equals OR exact_match
    
    :param str key: the key of the term.
    :param value: the value of the term.
    :rtype: ``dict``"""

    operator, negation = "", False
    lookup = {
        "__gt": "greater_than", "__lt": "less_than",
        "__gte": "greater_or_equal", "__lte": "less_or_equal",
        "__in": "in", "__range": "range",
        "__contains_phrase": "contains_phrase",
        "__contains_words": "contains_words",
        "__contains": "contains_phrase", "__exists": "exists",
    }
    for suffix, key_operator in lookup.items():
        if key.endswith(suffix):
            operator = key_operator
            key = key[:-len(suffix)]
            if suffix == "__range":
                value = {
                    "from": value[0], "to": value[1],
                    "include_lower": isinstance(value, list),
                    "include_upper": isinstance(value, list),
                }
            if suffix == "__exists": negation = False if value else True
            break
    if key.endswith("__not"):
        negation = not negation
        key = key[:-5]
    key = key.replace("__", ".")
    if key not in TEXT_TERMS: raise ValueError(f"Invalid term: {key}")
    if not operator:
        is_numeric = "default-match" in TEXT_TERMS[key]
        operator = "equals" if is_numeric else "exact_match"
    parameters = {"attribute": key, "operator": operator}
    if operator != "exists": parameters["value"] = value
    if negation: parameters["negation"] = True
    return parameters


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