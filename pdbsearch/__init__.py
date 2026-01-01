import requests

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

def search(return_type, return_all=False):
    """Queries the RCSB search API.

    :param str return_type: the type of data to return.
    :param bool return_all: whether to return all results, unpaginated.
    :rtype: ``dict``"""

    query = {
        "return_type": return_type,
    }
    if return_all:
        query["request_options"] = {"return_all_hits": True}
    return send_request(query)


def send_request(query):
    """Sends a query dictionary to the RCSB search API. If a valid response is
    received, this will be returned in JSON format. Otherwise ``None`` will be
    returned.
    
    :param dict query: the query, formatted to RCSB specifications.
    :rtype: ``dict``"""

    response = requests.post(SEARCH_URL, json=query)
    if response.status_code == 200:
        return response.json()