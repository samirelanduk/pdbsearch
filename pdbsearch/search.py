import requests
import json

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