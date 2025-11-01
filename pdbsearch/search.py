import requests
from typing import Any, Callable

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

def search(return_type, ids_only=False, **kwargs):
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
    result = response.json()
    if ids_only:
        return [r["identifier"] for r in result["result_set"]]
    else:
        return result



function_names = {
    "entry": "entries",
    "polymer_entity": "polymer_entities",
    "non_polymer_entity": "non_polymer_entities",
    "polymer_instance": "polymer_instances",
    "assembly": "assemblies",
    "mol_definition": "mol_definitions",
}



def create_return_type_function(return_type):
    def function(**kwargs):
        return search(return_type, **kwargs)
    return function

entries = create_return_type_function("entry")
polymer_entities = create_return_type_function("polymer_entity")
non_polymer_entities = create_return_type_function("non_polymer_entity")
polymer_instances = create_return_type_function("polymer_instance")
assemblies = create_return_type_function("assembly")
mol_definitions = create_return_type_function("mol_definition")
