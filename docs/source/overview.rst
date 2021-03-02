Overview
--------

pdbsearch is a Python library for searching for PDB structures using the
RCSB web services.

Returning all PDB Codes
~~~~~~~~~~~~~~~~~~~~~~~

You can get all PDB codes without any particular search expression like so:

    >>> import pdbsearch
    >>> codes = pdbsearch.search(limit=None)
    >>> len(codes)
    174994

This will take a few seconds, and requires downloading a rather large JSON
object over the network. Generally it is better to paginate the results:

    >>> first_ten_codes = pdbsearch.search(limit=10)
    >>> second_ten_codes = pdbsearch.search(start=10, limit=10)
    >>> third_ten_codes = pdbsearch.search(start=20, limit=10)
