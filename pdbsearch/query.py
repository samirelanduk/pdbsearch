
def get_text_parameters(key, value):
    """Constructs the parameters dictionary for a text service query.

    :param str key: the keyword argument passed to the search function.
    :param value: the search value.
    :rtype: ``dict``"""

    operator = "exact_match"
    lookup = {
        "__in": "in", 
        "__gt": "greater",
        "__gte": "greater_or_equal",
        "__lt": "less",
        "__lte": "less_or_equal",
        "__eq": "equals",
        "__exists": "exists",
        "__contains_words": "contains_words",
        "__contains_phrase": "contains_phrase",
    }
    for k, v in lookup.items():
        if key.endswith(k):
            key = key.replace(k, "")
            operator = v
            break
    if negation := key.endswith("__not"): key = key.replace("__not", "")
    key = key.replace("__", ".")
    parameters = {"attribute": key, "operator": operator, "value": value}
    if negation: parameters["negation"] = True
    if operator == "exists":
        del parameters["value"]
        if value == False: parameters["negation"] = True
    return parameters