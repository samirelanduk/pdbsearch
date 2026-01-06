import json
import os
import time
import requests

SCHEMA_FETCH_TIMEOUT = 2
CACHE_EXPIRY_SECONDS = 86400  # 24 hours
CACHE_FILE = os.path.join(os.path.dirname(__file__), ".terms_cache.json")

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
    processed = _process_schema_object(data)
    return _get_attribute_names(processed)


def update_terms_from_api():
    """Attempts to update the terms in the terms module, using cached values if
    available and not expired, otherwise fetching from the RCSB API. This
    function is called at import time and fails silently if the API is
    unreachable or returns invalid data.

    Returns ``True`` if both schemas were updated, ``False`` otherwise.

    :rtype: ``bool``"""

    from pdbsearch import terms
    cache = _load_cached_terms()
    if cache:
        terms.TEXT_TERMS.clear()
        terms.TEXT_TERMS.update(cache["text_terms"])
        terms.TEXT_CHEM_TERMS.clear()
        terms.TEXT_CHEM_TERMS.update(cache["chem_terms"])
        return True
    try:
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
        _save_cached_terms(new_text_terms, new_chem_terms)
        return True
    except Exception:
        return False


def clear_cached_terms():
    """Clears the cached terms."""

    try:
        os.remove(CACHE_FILE)
    except Exception:
        pass


def _load_cached_terms():
    """Loads cached terms from the cache file if it exists and is not expired.

    :rtype: ``dict`` or ``None``"""

    try:
        with open(CACHE_FILE) as f:
            cache = json.load(f)
        if time.time() - cache.get("timestamp", 0) < CACHE_EXPIRY_SECONDS:
            return cache
    except Exception:
        pass
    return None


def _save_cached_terms(text_terms, chem_terms):
    """Saves terms to the cache file with a timestamp.

    :param text_terms: The text terms dictionary.
    :param chem_terms: The chemical terms dictionary."""

    try:
        cache = {
            "timestamp": time.time(),
            "text_terms": text_terms,
            "chem_terms": chem_terms,
        }
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)
    except Exception:
        pass


def _process_schema_object(obj):
    """Strips down the schema object to get just the key attributes, with the
    same structure and nesting as the original object.

    :param obj: The schema object to process.
    :rtype: ``dict``"""

    if obj.get("type") == "array": return _process_schema_object(obj["items"])
    if obj.get("type") == "object":
        o = {}
        for key, value in obj["properties"].items():
            if processed := _process_schema_object(value): o[key] = processed
        return o
    if search := obj.get("rcsb_search_context"):
        return {
            "type": obj.get("type", [t["type"] for t in obj.get("anyOf", [])]),
            "description": obj.get("description", ""),
            "search": search,
            "is_terminal": True
        }


def _get_attribute_names(obj, prefix=""):
    """Takes the processed schema object returned by ``_process_schema_object``,
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
            names.update(_get_attribute_names(v, prefix=value))
    return names