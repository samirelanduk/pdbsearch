import requests

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

def search(return_type, ids_only=False, return_all=False, start=None, rows=None, text=None, **kwargs):
    query = {
        "return_type": return_type,
    }

    nodes = []
    if text:
        nodes.append({
            "type": "terminal",
            "service": "full_text",
            "parameters": {
                "value": text
            }
        })
    if kwargs:
        for key, value in kwargs.items():
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
            negation = False
            if key.endswith("__not"):
                key = key.replace("__not", "")
                negation = True
            key = key.replace("__", ".")
            nodes.append({
                "service": "text",
                "type": "terminal",
                "parameters": {
                    "attribute": key,
                    "operator": operator,
                    "value": value
                }
            })
            if operator == "exists":
                del nodes[-1]["parameters"]["value"]
                if value == False:
                    nodes[-1]["parameters"]["negation"] = True
            if negation:
                nodes[-1]["parameters"]["negation"] = True
    
    if len(nodes) == 1:
        query["query"] = nodes[0]
    elif len(nodes) > 1:
        query["query"] = {
            "type": "group",
            "logical_operator": "and",
            "nodes": nodes
        }

    if request_options := create_request_options(return_all, start, rows):
        query["request_options"] = request_options
    return send_query(query, ids_only)


def create_request_options(return_all=False, start=None, rows=None):
    options = {}
    if return_all: options["return_all_hits"] = True
    if start is not None or rows is not None:
        options["paginate"] = {}
        if start is not None: options["paginate"]["start"] = start
        if rows is not None: options["paginate"]["rows"] = rows
    return options if options else None


def send_query(query, ids_only=False):
    """Sends a structured query object to the RCSB search API, and processes the
    response.

    :param dict query: the query object to send.
    :param bool ids_only: whether to return only the identifiers of the results.
    :rtype: ``list`` or ``dict``"""

    response = requests.post(SEARCH_URL, json=query)
    if response.status_code == 204: return None
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
