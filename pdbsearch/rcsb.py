import requests
import json

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v1/query?json="

def search(start=0, limit=10):
    """Searches for PDB codes. You can choose how many to get and from what
    starting point.

    :param int start: the start index (default 0).
    :param int limit: how many codes to return (default 10).
    :rtype: ``list``"""
    
    query = {}
    query["return_type"] = "entry"
    query["query"] = {"type": "terminal", "service": "text"}
    if limit:
        query["request_options"] = {"pager": {"start": start, "rows": limit}}
    else:
        query["request_options"] = {"return_all_hits": True}
    response = requests.get(SEARCH_URL + json.dumps(query))
    if response.status_code == 200:
        result = response.json()
        return [r["identifier"] for r in result["result_set"]]
