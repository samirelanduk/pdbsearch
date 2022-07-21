import requests
import json

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query?json="

SUFFIXES = {
    "lte": "less_or_equal",
    "lt": "less",
    "gte": "greater_or_equal",
    "gt": "greater",
    "within": "range",
    "in": "in",
}

QUERY_SHORTHAND  = {
    "ligand_name": "rcsb_nonpolymer_instance_feature_summary.comp_id",
    "ligand_distance": "rcsb_ligand_neighbors.distance",
    "released": "rcsb_accession_info.initial_release_date",
    "deposited": "rcsb_accession_info.deposit_date",
    "code": "rcsb_entry_container_identifiers.entry_id",
    "atoms": "rcsb_entry_info.deposited_atom_count",
    "resolution": "rcsb_entry_info.resolution_combined"
}

def search(start=0, limit=10, sort=None, **kwargs):
    """Searches for PDB codes. You can choose how many to get and from what
    starting point.

    Sort terms can either be formal RCSB attributes, or a shorthand such as
    'resolution' or 'code'. If you supply a list of terms, these will be
    applied in turn.

    :param int start: the start index (default 0).
    :param int limit: how many codes to return (default 10).
    :param sort: the sort term, or list of sort terms.
    :rtype: ``list``"""
    
    query = {}
    query["return_type"] = "entry"
    apply_pagination(query, start, limit)
    apply_sort(query, sort)
    apply_query(query, kwargs)
    result = send_request(query)
    if result: return [r["identifier"] for r in result["result_set"]]


def apply_pagination(query, start, limit):
    """Creates a query's ``request_options`` and applies pagination information
    to it, or an instruction to get all data.

    :param dict query: the RCSB query object.
    :param int start: the start location.
    :param int limit: the number of results to return (or ``None`` to get \
    everything)"""

    if limit:
        query["request_options"] = {"paginate": {"start": start, "rows": limit}}
    else:
        query["request_options"] = {"return_all_hits": True}


def apply_sort(query, sort):
    """Applies sort terms to a query's ``request_options``.

    :param dict query: the RCSB query object.
    :param sort: the sort term(s)."""

    if not sort: return
    if isinstance(sort, str): sort = [sort]
    query["request_options"]["sort"] = [sort_term_to_sort_dict(s) for s in sort]


def sort_term_to_sort_dict(term):
    """Converts a single string to a RCSB sort modifier. If a '-' is on the
    front of the string, the search will be made ascending - otherwise it is
    descending.

    The string should be one of the terms given at
    `<https://search.rcsb.org/search-attributes.html>`_, or one of a few
    shorthands (see code).

    :param str term: the sort term.
    :rtype: ``dict``"""

    direction = "desc"
    if term[0] == "-":
        direction = "asc"
        term = term[1:]
    return {"sort_by": QUERY_SHORTHAND.get(term, term), "direction": direction}


def apply_query(query, kwargs):
    """Adds the query component to the overall query object. It uses whatever
    leftover keyword arguments are passed to the search function and uses these
    in a chain of AND queries.

    :param dict query: the RCSB query object.    
    :param dict kwargs: the keyword arguments passed to the search function."""

    query["query"] = {"type": "group", "logical_operator": "and", "nodes": []}
    for kwarg, value in kwargs.items():
        parameters = get_query_parameters(kwarg, value)
        if parameters:
            query["query"]["nodes"].append({
                "type": "terminal", "service": "text", "parameters": parameters
            })
    if not query["query"]["nodes"]:
        query["query"] = {"type": "terminal", "service": "text"}


def get_query_parameters(property, value):
    """Takes a key-value pair passed to the search function and turns it into a
    parameters dictionary representing that search criterion.

    :param str property: the keyword name.
    :param value: the search value.
    :rtype: ``dict``"""

    attribute = get_query_attribute(property)
    operator = get_query_operator(property, value)
    if operator == "range": value = {"from": value[0], "to": value[1]}
    return {"attribute": attribute, "operator": operator, "value": value}


def get_query_attribute(kwarg):
    """Takes a proposed query property and modifies it as needed based on
    suffixes or shorthand.

    :param str kwarg: the keyword argument passed to the search function.
    :rtype: ``str``"""
    
    attribute = kwarg
    for suffix in SUFFIXES:
        attribute = attribute.replace(f"__{suffix}", "")
    attribute = attribute.replace("__", ".")
    if attribute in QUERY_SHORTHAND: attribute = QUERY_SHORTHAND[attribute]
    return attribute


def get_query_operator(kwarg, value):
    """Takes a key-value pair passed to the search function and works out what
    operator should be used (equals, less than, within etc.).

    :param str kwarg: the keyword argument passed to the search function.
    :param value: the search value.
    :rtype: ``str``"""

    operator = "exact_match"
    if isinstance(value, int) or isinstance(value, float):
        operator = "equals"
    for suffix in SUFFIXES:
        if kwarg.endswith(f"__{suffix}"):
            operator = SUFFIXES[suffix]
    return operator


def send_request(query):
    """Sends a query dictionary to the RCSB search API. If a valid response is
    received, this will be returned in JSON format. Otherwise ``None`` will be
    returned.
    
    :param dict query: the query, formatted to RCSB specifications.
    :rtype: ``dict``"""

    response = requests.get(SEARCH_URL + json.dumps(query))
    if response.status_code == 200:
        return response.json()