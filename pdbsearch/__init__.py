import requests

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

def search(return_type):
    """Queries the RCSB search API.

    :param str return_type: the type of data to return.
    :rtype: ``dict``"""

    query = {
        "return_type": return_type,
    }
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