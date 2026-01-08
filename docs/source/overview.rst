Overview
--------

pdbsearch is a Python library for searching for PDB structures using the
RCSB web services.

Basic Search
~~~~~~~~~~~~

The default search will return PDB entry IDs, with no filtering:

    >>> import pdbsearch
    >>> results = pdbsearch.search()
    >>> print(results)
    {'query_id': '9a0c3543-0e29-462c-8357-f286293d9896', 'result_type': 'entry',
     'total_count': 247417, 'result_set': [{'identifier': '100D', 'score': 1.0},
     {'identifier': '101D', 'score': 1.0}, {'identifier': '101M', 'score': 1.0},
     {'identifier': '102D', 'score': 1.0}, {'identifier': '102L', 'score': 1.0},
     {'identifier': '102M', 'score': 1.0}, {'identifier': '103D', 'score': 1.0},
     {'identifier': '103L', 'score': 1.0}, {'identifier': '103M', 'score': 1.0},
     {'identifier': '104D', 'score': 1.0}]}

The JSON returned is the direct output from the RCSB search API. By default, it
returns 10 results at a time.

Services
########

RCSB defines a number of services which search in different ways. For example,
the full text search service will search the entire PDB database for the given
term, and you can access this with the ``term`` keyword argument:

    >>> results = pdbsearch.search(term="thymidine kinase")

You can search for entries with other services, using the correct keyword
arguments:

    >>> # Sequence service
    >>> results = pdbsearch.search(protein="MALWMRLLPLLALLALWGPDPAAA")
    >>> results = pdbsearch.search(dna="ATGC", identity=0.95, evalue=1e-10)
    >>> results = pdbsearch.search(rna="AUGC")
    >>>
    >>> # Sequence motif service
    >>> results = pdbsearch.search(protein="C-X-C-X(2)-[LIVMYFWC]", pattern_type="prosite")
    >>> results = pdbsearch.search(dna="GTXXCA", pattern_type="simple")
    >>> results = pdbsearch.search(rna="AUG{2}C", pattern_type="regex")
    >>>
    >>> # Structure service (requires the ID of a specific assembly to look for)
    >>> results = pdbsearch.search(structure="1A2B-2", operator="relaxed_shape_match")
    >>>
    >>> # Structure motif service (requires a residue pattern in some entry)
    >>> results = pdbsearch.search(entry="1A2B", residues=(("A", 1), ("B", 2)))
    >>>
    >>> # Chemical service
    >>> results = pdbsearch.search(smiles="CC(C)C", match_type="graph-relaxed-stereo")
    >>> results = pdbsearch.search(inchi="InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2")

The most useful service however, is the text service. The documentation for the
RCSB search API lists a number of attributes that you can search on, and which
can be viewed `here <https://search.rcsb.org/structure-search-attributes.html>`_.
For example, ``pdbx_entity_nonpoly.name`` or
``rcsb_nonpolymer_entity.pdbx_number_of_molecules``. You pass these as keyword
arguments to the :py:func:`pdbsearch.search` function, with the prefix ``__``
in place of the dot.

    >>> results = pdbsearch.search(pdbx_entity_nonpoly__name="glucose")
    >>> results = pdbsearch.search(rcsb_nonpolymer_entity__pdbx_number_of_molecules=0)

As the `RCSB documentation <https://search.rcsb.org/#search-api>`_ indicates, you can use a variety of operators to
modify how you search, and these are encoded as suffixes to the keyword
arguments:

- ``__gt``: ``greater``
- ``__lt``: ``less``
- ``__gte``: ``greater_or_equal``
- ``__lte``: ``less_or_equal``
- ``__in``: ``in``
- ``__exists``: ``exists``
- ``__range``: ``range`` (use ``tuple`` for exclusive range, ``list`` for inclusive range)
- ``__contains``: ``contains_phrase``
- ``__contains_phrase``: ``contains_phrase``
- ``__contains_words``: ``contains_words``
- ``__not``: ``not``

You can also use the ``__not`` suffix to negate the search.

    >>> results = pdbsearch.search(pdbx_entity_nonpoly__name__not="glucose")
    >>> results = pdbsearch.search(rcsb_nonpolymer_entity__pdbx_number_of_molecules__not=0)

There is a very similar search service called the ``text_chem`` service, which
has a different set of `attributes <https://search.rcsb.org/chemical-search-attributes.html>`_
(in practice a subset of the structure attributes) but which works the
same way. It searches properties of chemical compounds, such as formula weight.
The ``search`` function will default to using this service if you are searching
for small molecules.

    >>> results = pdbsearch.search(return_type="mol_definition", chem_comp__formula_weight__lt=1000)

Return Types
############

The above examples all search for entries (i.e. PDB files) but the RCSB API
also lets you search for other types of objects, such as polymer entities,
non-polymer entities, and chemical compounds.

The type of object you search for is determined by the ``return_type`` parameter.
The possible values are: ``entry``, ``assembly``, ``polymer_entity``,
``non_polymer_entity``, ``polymer_instance``, ``mol_definition``. Where the term
you are searching for does not correspond to the type of object you are
searching for (i.e. doing a sequence search but asking for non-polymer
entities), the API will use entries as a base (i.e finding all entries with a
polymer entity matching your sequence, and then returning all non-polymer
entities in those entries).

Alternatively, there are specific functions for searching for each of these types
of objects - ``pdbsearch.search_entries``, ``pdbsearch.search_assemblies``, etc.

Multiple Queries
################

You can combine any of the above parameters to search multiple services at once.
These will be combined with an ``and`` operator.

    >>> results = pdbsearch.search(
        return_type="polymer_entity",
        term="thymidine kinase",
        chem_comp__formula_weight__lt=1000,
        pdbx_struct_assembly__details__not__contains="good",
        protein="MALWMRLLPLLALLALWGPDPAAA",
        dna="ATGC",
        rna="AUGC",
        identity=0.95,
        evalue=1e-10,
        structure="1A2B-2",
        operator="relaxed_shape_match",
        entry="1A2B",
        residues=(("A", 1), ("B", 2)),
        rmsd=0.5,
        exchanges={("A", 1): ["ASP"], ("B", 2): ["HIS"]},
        smiles="CC(C)C",
        inchi="InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2",
        match_type="graph-relaxed-stereo",
    )

Request Options
################

You can control how the search is performed and returned with various request
option parameters:

    >>> # Return all results in one response
    >>> results = pdbsearch.search(term="thymidine kinase", return_all=True)
    >>>
    >>> # Return only the count of results
    >>> results = pdbsearch.search(term="thymidine kinase", counts_only=True)
    >>>
    >>> # Return results starting from the 10th result
    >>> results = pdbsearch.search(term="thymidine kinase", start=10)
    >>>
    >>> # Return 20 results at a time
    >>> results = pdbsearch.search(term="thymidine kinase", rows=20)
    >>>
    >>> # Sort results by the deposit date (descending)
    >>> results = pdbsearch.search(term="thymidine kinase", sort="-rcsb_accession_info.deposit_date")
    >>>
    >>> # Sort results by the polymer entity count (ascending)
    >>> results = pdbsearch.search(term="thymidine kinase", sort="rcsb_assembly_info.polymer_entity_count")
    >>>
    >>> # Sort results by multiple attributes
    >>> results = pdbsearch.search(term="thymidine kinase", sort=["-rcsb_accession_info.deposit_date", "rcsb_assembly_info.polymer_entity_count"])
    >>>
    >>> # Return results with computational content type only
    >>> results = pdbsearch.search(term="thymidine kinase", content_types=["computational"])
    >>>
    >>> # Use the API's facets functionality (see their documentation for more details)
    >>> results = pdbsearch.search(term="thymidine kinase", facets=[...])

Nodes and Queries
~~~~~~~~~~~~~~~~~

The :py:func:`pdbsearch.search` function is useful for simple queries, but it has some limitations.

1. If using multiple queries, they will always be combined with an `and` operator.
2. You can only provide one value per argument - if you have multiple protein sequences, you can't search for them all at once.

It can sometimes be useful to access the underlying node system that
:py:func:`pdbsearch.search` is built on for more complex queries. This solves
both of the above limitations.

Nodes
#####

Each of the search services has a function for creating a single search node.

    >>> # Full text search node
    >>> node = pdbsearch.full_text_node(term="thymidine kinase")
    >>>
    >>> # Text search node
    >>> node = pdbsearch.text_node(pdbx_struct_assembly__details__not__contains="good")
    >>>
    >>> # Text chem search node
    >>> node = pdbsearch.text_chem_node(chem_comp__formula_weight__lt=1000)
    >>>
    >>> # Sequence search nodes
    >>> node = pdbsearch.sequence_node(protein="MALWMRLLPLLALLALWGPDPAAA", identity=0.95, evalue=1e-10)
    >>> node = pdbsearch.sequence_node(dna="ATGC", identity=0.95, evalue=1e-10)
    >>> node = pdbsearch.sequence_node(rna="AUGC", identity=0.95, evalue=1e-10)
    >>>
    >>> # Sequence motif search node
    >>> node = pdbsearch.seqmotif_node(protein="C-X-C-X(2)-[LIVMYFWC]", pattern_type="prosite")
    >>>
    >>> # Structure search node
    >>> node = pdbsearch.structure_node("1A2B-2", operator="relaxed_shape_match")
    >>>
    >>> # Structure motif search node
    >>> node = pdbsearch.strucmotif_node("1A2B", residues=(("A", 1), ("B", 2)), rmsd=0.5, exchanges={("A", 1): ["ASP"], ("B", 2): ["HIS"]})
    >>>
    >>> # Chemical search nodes
    >>> node = pdbsearch.chemical_node(smiles="CC(C)C", match_type="graph-relaxed-stereo")
    >>> node = pdbsearch.chemical_node(inchi="InChI=1S/C6H12/c1-2-4-6-5-3-1/h1-6H2", match_type="graph-relaxed-stereo")

You can execute any of these nodes individually using their
:py:func:`pdbsearch.query` method. These can take a ``return_type`` parameter,
and all of the request option parameters.

    >>> results = node.query("entry", return_all=True, sort="-rcsb_accession_info.deposit_date")

Combining Nodes
###############

All node objects have an ``and_`` and ``or_`` method, which can be used to combine
them with other nodes.

    >>> node1 = pdbsearch.full_text_node(term="thymidine kinase")
    >>> node2 = pdbsearch.text_node(pdbx_struct_assembly__details__not__contains="good")
    >>> node3 = pdbsearch.sequence_node(protein="MALWMRLLPLLALLALWGPDPAAA", identity=0.95, evalue=1e-10)
    >>> node4 = pdbsearch.sequence_node(dna="ATGC", identity=0.95, evalue=1e-10)
    >>> node5 = pdbsearch.sequence_node(rna="AUGC", identity=0.95, evalue=1e-10)
    >>> node = node1.and_(node2).or_(node3.and_(node4.or_(node5)))
    >>> results = node.query("entry", return_all=True, sort="-rcsb_accession_info.deposit_date")

Schemas
~~~~~~~

The text and text_chem services have a schema that defines the attributes you can
search on. These can be read `here <https://search.rcsb.org/structure-search-attributes.html>`_
and `here <https://search.rcsb.org/chemical-search-attributes.html>`_ respectively.

They are also available as JSON schema objects,
`here <https://search.rcsb.org/rcsbsearch/v2/metadata/schema>`_ and
`here <https://search.rcsb.org/rcsbsearch/v2/metadata/chemical/schema>`_
respectively. This is important as pdbsearch needs to know type information
about the attributes in order to know which operator to use sometimes, and it
needs to know which parameter names correspond to this service when parsing a
:py:func:`pdbsearch.search` function call.

For this reason, a simplified form of the schema (all attributes, but only the
information about them pdbsearch needs) is hardcoded into the library. To ensure
the library always uses the most up to date information, it will try to update
its own local copy of the schema from the RCSB API when the library is imported.

This can be disabled by setting the ``PDBSEARCH_NO_UPDATE`` environment variable.

You can also download the full schema using a CLI command::

    pdbsearch schema > schema.json
    pdbsearch schema --chemical --indent 4 > chemical_schema.json

The downloaded schema information will be cached locally, so that it doesn't fetch
the schema every time pdbsearch runs - to delete this local cache, you can run::

    pdbsearch clearschema
