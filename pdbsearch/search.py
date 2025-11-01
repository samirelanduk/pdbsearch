import requests

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

def search(return_type, ids_only=False, **kwargs):
    query = {
        "return_type": return_type,
    }
    if len(kwargs) == 1:
        key, value = kwargs.popitem()
        if key.endswith("__in"):
            key = key.replace("__in", "")
            operator = "in"
        elif key.endswith("__gt"):
            key = key.replace("__gt", "")
            operator = "greater"
        elif key.endswith("__gte"):
            key = key.replace("__gte", "")
            operator = "greater_or_equal"
        elif key.endswith("__lt"):
            key = key.replace("__lt", "")
            operator = "less"
        elif key.endswith("__lte"):
            key = key.replace("__lte", "")
            operator = "less_or_equal"
        elif key.endswith("__eq"):
            key = key.replace("__eq", "")
            operator = "equals"
        elif key.endswith("__exists"):
            key = key.replace("__exists", "")
            operator = "exists"
        elif key.endswith("__contains_words"):
            key = key.replace("__contains_words", "")
            operator = "contains_words"
        elif key.endswith("__contains_phrase"):
            key = key.replace("__contains_phrase", "")
            operator = "contains_phrase"
        else:
            operator = "exact_match"
        key = key.replace("__", ".")
        query["query"] = {
            "type": "terminal",
            "service": "text",
            "parameters": {
                "attribute": key,
                "operator": operator,
                "value": value
            }
        }
        if operator == "exists":
            del query["query"]["parameters"]["value"]
    response = requests.post(SEARCH_URL, json=query)
    result = response.json()
    if ids_only:
        return [r["identifier"] for r in result["result_set"]]
    else:
        return result



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
