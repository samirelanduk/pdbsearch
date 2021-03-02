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

Table of Contents
-----------------

.. toctree ::
  installing
  overview
  api
  changelog
