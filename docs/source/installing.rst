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
