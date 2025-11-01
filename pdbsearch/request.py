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