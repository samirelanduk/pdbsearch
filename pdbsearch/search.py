import requests

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

def search(return_type, **kwargs):
    query = {
        "return_type": return_type,
    }
    if len(kwargs) == 1:
        key, value = kwargs.popitem()
        key = key.replace("__", ".")
        query["query"] = {
            "type": "terminal",
            "service": "text",
            "parameters": {
                "attribute": key,
                "operator": "exact_match",
                "value": value
            }
        }
    response = requests.post(SEARCH_URL, json=query)
    return response.json()


def entries(**kwargs):
    return search("entry", **kwargs)


def polymer_entities(**kwargs):
    return search("polymer_entity", **kwargs)


def non_polymer_entities(**kwargs):
    return search("non_polymer_entity", **kwargs)


def polymer_instances(**kwargs):
    return search("polymer_instance", **kwargs)


def assemblies(**kwargs):
    return search("assembly", **kwargs)


def mol_definitions(**kwargs):
    return search("mol_definition", **kwargs)