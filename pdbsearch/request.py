import requests

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

def send_request(request, ids_only=False):
    """Sends a structured query request object to the RCSB search API, and
    processes the response.

    :param dict request: the query request object to send.
    :param bool ids_only: whether to return only the identifiers of the results.
    :rtype: ``list`` or ``dict``"""

    response = requests.post(SEARCH_URL, json=request)
    if response.status_code == 204: return None
    result = response.json()
    if ids_only:
        return [r["identifier"] for r in result["result_set"]]
    else:
        return result


def create_request_options(return_all=False, start=None, rows=None, counts_only=False):
    """Creates a request options dictionary for the RCSB search API.
    
    :param bool return_all: whether to return all hits rather than paginating.
    :param int start: the start index for pagination.
    :param int rows: the page size.
    :param bool counts_only: whether to return only the results count.
    :rtype: ``dict``"""
    
    options = {}
    if return_all: options["return_all_hits"] = True
    if counts_only: options["return_counts"] = True
    if start is not None or rows is not None:
        options["paginate"] = {}
        if start is not None: options["paginate"]["start"] = start
        if rows is not None: options["paginate"]["rows"] = rows
    return options if options else None