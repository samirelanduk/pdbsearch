import sys
import requests

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

def query(return_type, node=None, **request_options):
    """Queries the RCSB search API.

    :param str return_type: the type of data to return.
    :param Node node: the node to query.
    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :param str or list[str] sort: the attribute or attributes to sort by.
    :param bool counts_only: whether to return only the count of results.
    :param list[str] content_types: the PDB types (experimental/computational).
    :rtype: ``dict``"""

    query = {"return_type": return_type}
    if node: query["query"] = node.serialize()
    if request_options := create_request_options(**request_options):
        query["request_options"] = request_options
    return send_request(query)


def create_request_options(return_all=False, start=None, rows=None, sort=None, counts_only=False, content_types=None):
    """Creates a request options dictionary for the RCSB search API.
    
    :param bool return_all: whether to return all results, unpaginated.
    :param int start: the start index of the results.
    :param int rows: the number of results to return.
    :param str or list[str] sort: the attribute or attributes to sort by.
    :param bool counts_only: whether to return only the count of results.
    :param list[str] content_types: the PDB types (experimental/computational).
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
    if sort:
        request_options["sort"] = [{
            "sort_by": attribute.replace("__", ".").lstrip("-"),
            "direction": "desc" if attribute.startswith("-") else "asc"
        } for attribute in ([sort] if isinstance(sort, str) else sort)]
    if counts_only: request_options["return_counts"] = True
    if content_types: request_options["results_content_type"] = content_types
    return request_options


def send_request(query):
    """Sends a query dictionary to the RCSB search API. If a valid response is
    received, this will be returned in JSON format. Otherwise the error message
    will be written to stderr, and an exception will be raised.
    
    :param dict query: the query, formatted to RCSB specifications.
    :rtype: ``dict``"""

    response = requests.post(SEARCH_URL, json=query)
    if response.status_code == 200:
        return response.json()
    if response.status_code == 204: return None
    try:
        print(response.json(), file=sys.stderr)
    except requests.exceptions.JSONDecodeError:
        print(
            response.status_code,
            response.content.decode() if len(response.content) < 100 else "",
            file=sys.stderr
        )
    response.raise_for_status()