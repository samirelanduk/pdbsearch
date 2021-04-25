pdbsearch
=========

|travis| |coveralls| |pypi| |version| |commit|

.. |travis| image:: https://api.travis-ci.org/samirelanduk/pdbsearch.svg?branch=master
  :target: https://travis-ci.org/samirelanduk/pdbsearch/

.. |coveralls| image:: https://coveralls.io/repos/github/samirelanduk/pdbsearch/badge.svg?branch=master
  :target: https://coveralls.io/github/samirelanduk/pdbsearch/

.. |pypi| image:: https://img.shields.io/pypi/pyversions/pdbsearch.svg
  :target: https://pypi.org/project/pdbsearch/

.. |version| image:: https://img.shields.io/pypi/v/pdbsearch.svg
  :target: https://pypi.org/project/pdbsearch/

.. |commit| image:: https://img.shields.io/github/last-commit/samirelanduk/pdbsearch/master.svg
  :target: https://github.com/samirelanduk/pdbsearch/tree/master/


pdbsearch is a Python library for searching for PDB structures using the
RCSB web services.

Example
-------

    >>> import pdbsearch
    >>> codes = pdbsearch.search(limit=5)
    >>> codes
    ['4CD7', '4CCW', '4CD8', '4CCX', '4CCY']



Installing
----------

pip
~~~

pdbsearch can be installed using pip (you may need to use ``pip3``):

``$ pip install pdbsearch``

If you get permission errors, try using ``sudo``:

``$ sudo pip install pdbsearch``


Development
~~~~~~~~~~~

The repository for pdbsearch, containing the most recent iteration, can be
found `here <http://github.com/samirelanduk/pdbsearch/>`_. To clone the
pdbsearch repository directly from there, use:

``$ git clone git://github.com/samirelanduk/pdbsearch.git``


Requirements
~~~~~~~~~~~~

pdbsearch requires `requests <http://docs.python-requests.org/>`_.


Testing
~~~~~~~

To test a local version of pdbsearch, cd to the pdbsearch directory and run:

``$ python -m unittest discover tests``

You can opt to only run unit tests or integration tests:

``$ python -m unittest discover tests.unit``
``$ python -m unittest discover tests.integration``


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





Changelog
---------

Release 0.2.0
~~~~~~~~~~~~~

`25 April 2021`

* Added ability to sort results.
* Created shorthand system for common sort criteria.


Release 0.1.0
~~~~~~~~~~~~~

`2 March 2021`

* Started library.
* Added ability to fetch all PDB codes.
* Basic pagination.