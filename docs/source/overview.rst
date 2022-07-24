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
`<https://search.rcsb.org/structure-search-attributes.html>`_:

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

Search Criteria
~~~~~~~~~~~~~~~

You can search by passing keywords to the search function:

    >>> pdbsearch.search(limit=5, ligand_name="ZN")
    ['3HW7', '3I7I', '3I7G', '2WFX', '2WGT']

You can modify the operator used with double underscores:

    >>> pdbsearch.search(limit=5, ligand_name__in=["ZN", "CU"])
    ['3HW7', '3I7I', '3I7G', '2WFX', '2WGT']
    >>> pdbsearch.search(limit=5, resolution__lt=2)
    ['3HW3', '3I83', '3HVS', '3HW4', '3HW5']
    >>> pdbsearch.search(limit=5, atoms__within=[200, 300])
    ['2WH9', '2WPY', '395D', '396D', '2X8Q']

These are some shorthands, but you can search by any of the terms in the above
linked list by replacing the dot with a double underscore:

    >>> pdbsearch.search(limit=5, citation__rcsb_authors="Sula, A.")
    ['4CAH', '4CAI', '4X8A', '4X88', '4X89']

If you use more than one term, they will be combined with AND operators:

    >>> pdbsearch.search(limit=5, ligand_name="ZN", atoms__within=[200, 300])
    ['3WUP', '3ZNF', '2YTA', '2YTB', '2YSV']