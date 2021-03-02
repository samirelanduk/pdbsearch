import requests
import json

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v1/query?json="

def codes():
    query = {
        "query": {"type": "terminal", "service": "text"},
        "request_options": {"return_all_hits": True},
        "return_type": "entry"
    }
    url = "https://search.rcsb.org/rcsbsearch/v1/query?json="
    return [pdb["identifier"] for pdb in requests.get(
        url + json.dumps(query)
    ).json()["result_set"]]


def search(start=0, limit=10):
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
