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

You can sort the results by any of the terms at
`<https://search.rcsb.org/search-attributes.html>`_:

    >>> most_recent_codes = pdbsearch.search(sort="rcsb_accession_info.deposit_date")
    >>> earliest_codes = pdbsearch.search(sort="-rcsb_accession_info.deposit_date")

As these are somewhat cumbersome, some of them have a shorthand:

    >>> pdbsearch.search(limit=5, sort="code")
    ['9XIM', '9XIA', '9WGA', '9RUB', '9RSA']
    >>> pdbsearch.search(limit=5, sort="-resolution")
    ['3NIR', '5D8V', '1EJG', '3P4J', '5NW3']

You can sort by multiple criteria:

    >>> pdbsearch.search(limit=5, sort=["-atoms", "released"])
    ['1ANP', '6UOU', '6UOW', '1Q7O', '6QTF']



