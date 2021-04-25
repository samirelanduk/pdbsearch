import requests
import json

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v1/query?json="

def search(start=0, limit=10, sort=None):
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
    query["query"] = {"type": "terminal", "service": "text"}
    apply_pagination(query, start, limit)
    apply_sort(query, sort)
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
        query["request_options"] = {"pager": {"start": start, "rows": limit}}
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

    shorthand = {
        "released": "rcsb_accession_info.initial_release_date",
        "deposited": "rcsb_accession_info.deposit_date",
        "code": "rcsb_entry_container_identifiers.entry_id",
        "atoms": "rcsb_entry_info.deposited_atom_count",
        "resolution": "rcsb_entry_info.resolution_combined"
    }
    direction = "desc"
    if term[0] == "-":
        direction = "asc"
        term = term[1:]
    return {"sort_by": shorthand.get(term, term), "direction": direction}


def send_request(query):
    """Sends a query dictionary to the RCSB search API. If a valid response is
    received, this will be returned in JSON format. Otherwise ``None`` will be
    returned.
    
    :param dict query: the query, formatted to RCSB specifications.
    :rtype: ``dict``"""

    response = requests.get(SEARCH_URL + json.dumps(query))
    if response.status_code == 200:
        return response.json()

