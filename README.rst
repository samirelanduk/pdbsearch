pdbsearch
=========

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
    >>> codes = pdbsearch(limit=None)
    >>> len(codes)
    174994

This will take a few seconds, and requires downloading a rather large JSON
object over the network. Generally it is better to paginate the results:

    >>> first_ten_codes = pdbsearch.search(limit=10)
    >>> second_ten_codes = pdbsearch.search(start=10, limit=10)
    >>> third_ten_codes = pdbsearch.search(start=20, limit=10)



Changelog
---------

Release 0.1.0
~~~~~~~~~~~~~

`2 March 2021`

* Started library.
* Added ability to fetch all PDB codes.
* Basic pagination.