
def get_text_parameters(key, value):
    """Constructs the parameters dictionary for a text service query.

    The double-underscore suffix will determine the operator to use. For the
    range operator, [0, 1] lists denote inclusive ranges, (0, 1) tuples denote
    exclusive ranges.

    Any remaining double-underscores will be replaced with dots in the attribute
    name.

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
        "__between": "range",
    }
    for k, v in lookup.items():
        if key.endswith(k):
            key = key.replace(k, "")
            operator = v
            break
    if operator == "range":
        is_inclusive = isinstance(value, list)
        value = {"from": value[0], "to": value[1]}
        value["include_lower"] = value["include_upper"] = is_inclusive
    if negation := key.endswith("__not"): key = key.replace("__not", "")
    key = key.replace("__", ".")
    parameters = {"attribute": key, "operator": operator, "value": value}
    if negation: parameters["negation"] = True
    if operator == "exists":
        del parameters["value"]
        if value == False: parameters["negation"] = True
    return parameters