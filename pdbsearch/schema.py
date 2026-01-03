import requests

SCHEMA_FETCH_TIMEOUT = 2

def fetch_names_from_rcsb_schema(chemical=False, timeout=None):
    """Fetches the schema description object for either the text or text_chem
    service, and processes them down to the minimum information pdbsearch needs.

    :param chemical: Whether to fetch the chemical schema.
    :param timeout: Optional timeout for the request in seconds.
    :rtype: ``dict``"""

    text_url = "https://search.rcsb.org/rcsbsearch/v2/metadata/schema"
    chem_text_url = "https://search.rcsb.org/rcsbsearch/v2/metadata/chemical/schema"
    url = chem_text_url if chemical else text_url
    data = requests.get(url, timeout=timeout).json()
    processed = process_schema_object(data)
    return get_attribute_names(processed)


def update_terms_from_api():
    """Attempts to fetch the latest terms from the RCSB API and update the
    hardcoded terms in the terms module. This function is called at import time
    and fails silently if the API is unreachable or returns invalid data.

    Returns ``True`` if both schemas were updated, ``False`` otherwise.
    
    :rtype: ``bool``"""
    
    try:
        from pdbsearch import terms
        new_text_terms = fetch_names_from_rcsb_schema(
            chemical=False, timeout=SCHEMA_FETCH_TIMEOUT
        )
        new_chem_terms = fetch_names_from_rcsb_schema(
            chemical=True, timeout=SCHEMA_FETCH_TIMEOUT
        )
        terms.TEXT_TERMS.clear()
        terms.TEXT_TERMS.update(new_text_terms)
        terms.TEXT_CHEM_TERMS.clear()
        terms.TEXT_CHEM_TERMS.update(new_chem_terms)
        return True
    except Exception:
        return False


def process_schema_object(obj):
    """Strips down the schema object to get just the key attributes, with the
    same structure and nesting as the original object.

    :param obj: The schema object to process.
    :rtype: ``dict``"""

    if obj.get("type") == "array": return process_schema_object(obj["items"])
    if obj.get("type") == "object":
        o = {}
        for key, value in obj["properties"].items():
            if processed := process_schema_object(value): o[key] = processed
        return o
    if search := obj.get("rcsb_search_context"):
        return {
            "type": obj.get("type", [t["type"] for t in obj.get("anyOf", [])]),
            "description": obj.get("description", ""),
            "search": search,
            "is_terminal": True
        }


def get_attribute_names(obj, prefix=""):
    """Takes the processed schema object returned by ``process_schema_object``,
    and creates a mapping of API attribute names to their search contexts.

    :param obj: The processed schema object.
    :param prefix: The prefix to prepend when called recursively.
    :rtype: ``dict``"""

    names = {}
    for k, v in obj.items():
        value = f"{prefix}{'.' if prefix else ''}{k}"
        if v.get("is_terminal"):
            names[value] = v["search"]
        else:
            names.update(get_attribute_names(v, prefix=value))
    return names