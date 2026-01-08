pdbsearch
=========

pdbsearch is a Python library for searching for PDB structures using the
RCSB web services.

Example
-------

    >>> import pdbsearch
    >>> results = pdbsearch.search(rows=5, chem_comp__name__contains="zinc")
    >>> print(results["total_count"])
    26
    >>> print(results["result_set"])
    [{'identifier': '1A0B', 'score': 1.0}, {'identifier': '1A1F', 'score': 1.0},
     {'identifier': '1A1G', 'score': 1.0}, {'identifier': '1A1H', 'score': 1.0},
     {'identifier': '1A1I', 'score': 1.0}]

Table of Contents
-----------------

.. toctree ::
  installing
  overview
  api
  changelog
