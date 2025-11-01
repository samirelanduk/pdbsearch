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



function_names = {
    "entry": "entries",
    "polymer_entity": "polymer_entities",
    "non_polymer_entity": "non_polymer_entities",
    "polymer_instance": "polymer_instances",
    "assembly": "assemblies",
    "mol_definition": "mol_definitions",
}


for entity_type in function_names.keys():
    def dynamic_function(**kwargs):
        return search(entity_type, **kwargs)
    globals()[function_names[entity_type]] = dynamic_function