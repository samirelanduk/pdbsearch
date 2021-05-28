pdbsearch
=========

pdbsearch is a Python library for searching for PDB structures using the
RCSB web services.

Example
-------

    >>> import pdbsearch
    >>> codes = pdbsearch.search(limit=5, ligand_name="CU")
    >>> codes
    ['3HW7', '2WKO', '2WOF', '2WOH', '2WO0']

Table of Contents
-----------------

.. toctree ::
  installing
  overview
  api
  changelog
