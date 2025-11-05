RCSB_METADATA_SCHEMA = {
    "pdbx_entity_nonpoly": {
        "name": {
            "type": "string",
            "description": "A name for the non-polymer entity",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_nonpolymer_entity": {
        "details": {
            "type": "string",
            "description": "A description of special aspects of the entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "formula_weight": {
            "type": "number",
            "description": "Formula mass (KDa) of the entity.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "pdbx_description": {
            "type": "string",
            "description": "A description of the nonpolymer entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_number_of_molecules": {
            "type": "integer",
            "description": "The number of molecules of the nonpolymer entity in the entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_nonpolymer_entity_annotation": {
        "annotation_id": {
            "type": "string",
            "description": "An identifier for the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "comp_id": {
            "type": "string",
            "description": "Non-polymer(ligand) chemical component identifier for the entity.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "A description for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "A type or category of the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "annotation_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the annotation lineage as parent lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class identifiers.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class names.",
                "search": [
                    "exact-match",
                    "full-text"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_nonpolymer_entity_container_identifiers": {
        "chem_ref_def_id": {
            "type": "string",
            "description": "The chemical reference definition identifier for the entity in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "nonpolymer_comp_id": {
            "type": "string",
            "description": "Non-polymer(ligand) chemical component identifier for the entity in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "prd_id": {
            "type": "string",
            "description": "The BIRD identifier for the entity in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_id": {
            "type": "string",
            "description": "A unique identifier for each object in this entity container formed by\n an underscore separated concatenation of entry and entity identifiers.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_nonpolymer_entity_feature": {
        "type": {
            "type": "string",
            "description": "A type or category of the feature.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_nonpolymer_entity_feature_summary": {
        "count": {
            "type": "integer",
            "description": "The feature count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "Type or category of the feature.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_nonpolymer_entity_keywords": {
        "text": {
            "type": "string",
            "description": "Keywords describing this non-polymer entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_nonpolymer_entity_name_com": {
        "name": {
            "type": "string",
            "description": "A common name for the nonpolymer entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_id": {
        "type": "string",
        "description": "A unique identifier for each object in this entity container formed by\n an underscore separated concatenation of entry and entity identifiers.",
        "search": [
            "exact-match"
        ],
        "is_terminal": True
    },
    "chem_comp": {
        "formula_weight": {
            "type": "number",
            "description": "Formula mass of the chemical component.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "The full name of the component.",
            "search": [
                "exact-match",
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "For standard polymer components, the type of the monomer.\n Note that monomers that will form polymers are of three types:\n linking monomers, monomers with some type of N-terminal (or 5')\n cap and monomers with some type of C-terminal (or 3') cap.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_reference_molecule": {
        "class": {
            "type": "string",
            "description": "Broadly defines the function of the entity.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "Description of this molecule.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name of the entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "prd_id": {
            "type": "string",
            "description": "The value of _pdbx_reference_molecule.prd_id is the unique identifier\n for the reference molecule in this family.\n\n By convention this ID uniquely identifies the reference molecule in\n in the PDB reference dictionary.\n\n The ID has the template form PRD_dddddd (e.g. PRD_000001)",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "Defines the structural classification of the entity.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_reference_molecule_family": {
        "name": {
            "type": "string",
            "description": "The entity family name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_reference_molecule_related_structures": {
        "db_code": {
            "type": "string",
            "description": "The database identifier code for the related structure reference.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_reference_molecule_synonyms": {
        "name": {
            "type": "string",
            "description": "A synonym name for the entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_annotation": {
        "annotation_id": {
            "type": "string",
            "description": "An identifier for the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "A description for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "A type or category of the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "annotation_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the annotation lineage as parent lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class identifiers.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class names.",
                "search": [
                    "exact-match",
                    "full-text"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_chem_comp_container_identifiers": {
        "comp_id": {
            "type": "string",
            "description": "The chemical component identifier.",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        },
        "drugbank_id": {
            "type": "string",
            "description": "The DrugBank identifier corresponding to the chemical component.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "prd_id": {
            "type": "string",
            "description": "The BIRD definition identifier.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_id": {
            "type": "string",
            "description": "A unique identifier for the chemical definition in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_descriptor": {
        "InChIKey": {
            "type": "string",
            "description": "Standard IUPAC International Chemical Identifier (InChI) descriptor key\n for the chemical component\n\n InChI, the IUPAC International Chemical Identifier,\n by Stephen R Heller, Alan McNaught, Igor Pletnev, Stephen Stein and Dmitrii Tchekhovskoi,\n Journal of Cheminformatics, 2015, 7:23",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_info": {
        "atom_count_chiral": {
            "type": "integer",
            "description": "Chemical component chiral atom count",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "atom_count_heavy": {
            "type": "integer",
            "description": "Chemical component heavy atom count",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "bond_count": {
            "type": "integer",
            "description": "Chemical component total bond count",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "bond_count_aromatic": {
            "type": "integer",
            "description": "Chemical component aromatic bond count",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "initial_deposition_date": {
            "type": "string",
            "description": "The date the chemical definition was first deposited in the PDB repository.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "initial_release_date": {
            "type": "string",
            "description": "The initial date the chemical definition was released in the PDB repository.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_related": {
        "resource_accession_code": {
            "type": "string",
            "description": "The resource identifier code for the related chemical reference.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "resource_name": {
            "type": "string",
            "description": "The resource name for the related chemical reference.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_synonyms": {
        "name": {
            "type": "string",
            "description": "The synonym of this particular chemical component.",
            "search": [
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        },
        "provenance_source": {
            "type": "string",
            "description": "The provenance of this synonym.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "This data item contains the synonym type.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_target": {
        "name": {
            "type": "string",
            "description": "The chemical component target name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_struct_assembly": {
        "details": {
            "type": "string",
            "description": "A description of special aspects of the macromolecular assembly.\n\n               In the PDB, 'representative helical assembly', 'complete point assembly',\n\t       'complete icosahedral assembly', 'software_defined_assembly', 'author_defined_assembly',\n\t       and 'author_and_software_defined_assembly' are considered \"biologically relevant assemblies.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "oligomeric_details": {
            "type": "string",
            "description": "Provides the details of the oligomeric state of the assembly.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "rcsb_details": {
            "type": "string",
            "description": "A filtered description of the macromolecular assembly.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_struct_assembly_auth_evidence": {
        "details": {
            "type": "string",
            "description": "Provides any additional information regarding the evidence of this assembly",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "experimental_support": {
            "type": "string",
            "description": "Provides the experimental method to determine the state of this assembly",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_assembly_annotation": {
        "annotation_id": {
            "type": "string",
            "description": "An identifier for the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "A type or category of the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_assembly_container_identifiers": {
        "assembly_id": {
            "type": "string",
            "description": "Assembly identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entry_id": {
            "type": "string",
            "description": "Entry identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_id": {
            "type": "string",
            "description": "A unique identifier for each object in this assembly container formed by\n a dash separated concatenation of entry and assembly identifiers.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_assembly_info": {
        "atom_count": {
            "type": "integer",
            "description": "The assembly non-hydrogen atomic coordinate count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "branched_atom_count": {
            "type": "integer",
            "description": "The assembly non-hydrogen branched entity atomic coordinate count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "branched_entity_count": {
            "type": "integer",
            "description": "The number of distinct branched entities in the generated assembly.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "branched_entity_instance_count": {
            "type": "integer",
            "description": "The number of branched instances in the generated assembly data set.\n This is the total count of branched entity instances generated in the assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deuterated_water_count": {
            "type": "integer",
            "description": "The assembly deuterated water molecule count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "hydrogen_atom_count": {
            "type": "integer",
            "description": "The assembly hydrogen atomic coordinate count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "modeled_polymer_monomer_count": {
            "type": "integer",
            "description": "The number of modeled polymer monomers in the assembly coordinate data.\n This is the total count of monomers with reported coordinate data for all polymer\n entity instances in the generated assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "na_polymer_entity_types": {
            "type": "string",
            "description": "Nucleic acid polymer entity type categories describing the generated assembly.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "nonpolymer_atom_count": {
            "type": "integer",
            "description": "The assembly non-hydrogen non-polymer entity atomic coordinate count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "nonpolymer_entity_count": {
            "type": "integer",
            "description": "The number of distinct non-polymer entities in the generated assembly exclusive of solvent.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "nonpolymer_entity_instance_count": {
            "type": "integer",
            "description": "The number of non-polymer instances in the generated assembly data set exclusive of solvent.\n This is the total count of non-polymer entity instances generated in the assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_atom_count": {
            "type": "integer",
            "description": "The assembly non-hydrogen polymer entity atomic coordinate count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_composition": {
            "type": "string",
            "description": "Categories describing the polymer entity composition for the generated assembly.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count": {
            "type": "integer",
            "description": "The number of distinct polymer entities in the generated assembly.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count_DNA": {
            "type": "integer",
            "description": "The number of distinct DNA polymer entities in the generated assembly.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count_RNA": {
            "type": "integer",
            "description": "The number of distinct RNA polymer entities in the generated assembly.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count_nucleic_acid": {
            "type": "integer",
            "description": "The number of distinct nucleic acid polymer entities (DNA or RNA) in the generated assembly.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count_nucleic_acid_hybrid": {
            "type": "integer",
            "description": "The number of distinct hybrid nucleic acid polymer entities in the generated assembly.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count_protein": {
            "type": "integer",
            "description": "The number of distinct protein polymer entities in the generated assembly.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_instance_count": {
            "type": "integer",
            "description": "The number of polymer instances in the generated assembly data set.\n This is the total count of polymer entity instances generated in the assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_instance_count_DNA": {
            "type": "integer",
            "description": "The number of DNA polymer instances in the generated assembly data set.\n This is the total count of DNA polymer entity instances generated in the assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_instance_count_RNA": {
            "type": "integer",
            "description": "The number of RNA polymer instances in the generated assembly data set.\n This is the total count of RNA polymer entity instances generated in the assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_instance_count_nucleic_acid": {
            "type": "integer",
            "description": "The number of nucleic acid polymer instances in the generated assembly data set.\n This is the total count of nucleic acid polymer entity instances generated in the assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_instance_count_nucleic_acid_hybrid": {
            "type": "integer",
            "description": "The number of hybrid nucleic acide polymer instances in the generated assembly data set.\n This is the total count of hybrid nucleic acid polymer entity instances generated in the assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_instance_count_protein": {
            "type": "integer",
            "description": "The number of protein polymer instances in the generated assembly data set.\n This is the total count of protein polymer entity instances generated in the assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_monomer_count": {
            "type": "integer",
            "description": "The number of polymer monomers in sample entity instances comprising the assembly data set.\n This is the total count of monomers for all polymer entity instances\n in the generated assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "selected_polymer_entity_types": {
            "type": "string",
            "description": "Selected polymer entity type categories describing the generated assembly.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "solvent_atom_count": {
            "type": "integer",
            "description": "The assembly non-hydrogen solvent atomic coordinate count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "solvent_entity_count": {
            "type": "integer",
            "description": "The number of distinct solvent entities in the generated assembly.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "solvent_entity_instance_count": {
            "type": "integer",
            "description": "The number of solvent instances in the generated assembly data set.\n This is the total count of solvent entity instances generated in the assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "unmodeled_polymer_monomer_count": {
            "type": "integer",
            "description": "The number of unmodeled polymer monomers in the assembly coordinate data. This is\n the total count of monomers with unreported coordinate data for all polymer\n entity instances in the generated assembly coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_struct_symmetry": {
        "kind": {
            "type": "string",
            "description": "The granularity at which the symmetry calculation is performed. In 'Global Symmetry' all polymeric\n subunits in assembly are used. In 'Local Symmetry' only a subset of polymeric subunits is considered.\n In 'Pseudo Symmetry' the threshold for subunits similarity is relaxed.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "oligomeric_state": {
            "type": "string",
            "description": "Oligomeric state refers to a composition of polymeric subunits in quaternary structure.\n Quaternary structure may be composed either exclusively of several copies of identical subunits,\n in which case they are termed homo-oligomers, or alternatively by at least one copy of different\n subunits (hetero-oligomers). Quaternary structure composed of a single subunit is denoted as 'Monomer'.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "symbol": {
            "type": "string",
            "description": "Symmetry symbol refers to point group or helical symmetry of identical polymeric subunits in Schoenflies notation.\n Contains point group symbol (e.g., C2, C5, D2, T, O, I) or H for helical symmetry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "Symmetry type refers to point group or helical symmetry of identical polymeric subunits.\n Contains point group types (e.g. Cyclic, Dihedral) or Helical for helical symmetry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "clusters": {
            "avg_rmsd": {
                "type": "number",
                "description": "Average RMSD between members of a given cluster.",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_struct_symmetry_lineage": {
        "depth": {
            "type": "integer",
            "description": "Hierarchy depth.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "id": {
            "type": "string",
            "description": "Automatically assigned ID to uniquely identify the symmetry term in the Protein Symmetry Browser.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A human-readable term describing protein symmetry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_repository_holdings_current": {
        "repository_content_types": {
            "type": "string",
            "description": "The list of content types associated with this entry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_nonpolymer_entity_instance_container_identifiers": {
        "asym_id": {
            "type": "string",
            "description": "Instance identifier for this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "auth_asym_id": {
            "type": "string",
            "description": "Author instance identifier for this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "comp_id": {
            "type": "string",
            "description": "Component identifier for non-polymer entity instance.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entity_id": {
            "type": "string",
            "description": "Entity identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entry_id": {
            "type": "string",
            "description": "Entry identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_id": {
            "type": "string",
            "description": "A unique identifier for each object in this entity instance container formed by\n an 'dot' (.) separated concatenation of entry and entity instance identifiers.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_nonpolymer_instance_annotation": {
        "annotation_id": {
            "type": "string",
            "description": "An identifier for the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "comp_id": {
            "type": "string",
            "description": "Non-polymer (ligand) chemical component identifier.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "A description for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "A type or category of the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "annotation_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the annotation lineage as parent lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class identifiers.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class names.",
                "search": [
                    "exact-match",
                    "full-text"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_nonpolymer_instance_validation_score": {
        "RSCC": {
            "type": "number",
            "description": "The real space correlation coefficient (RSCC) for the non-polymer entity instance.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "RSR": {
            "type": "number",
            "description": "The real space R-value (RSR) for the non-polymer entity instance.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "intermolecular_clashes": {
            "type": "integer",
            "description": "The number of intermolecular MolProbity clashes cacluated for reported atomic coordinate records.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "is_best_instance": {
            "type": "string",
            "description": "This molecular instance is ranked as the best quality instance of this nonpolymer entity.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "is_subject_of_investigation": {
            "type": "string",
            "description": "This molecular entity is identified as the subject of the current study.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "mogul_angle_outliers": {
            "type": "integer",
            "description": "Number of bond angle outliers obtained from a CCDC Mogul survey of bond angles  in the CSD small\n   molecule crystal structure database. Outliers are defined as bond angles that have a Z-score\n   less than -2 or greater than 2.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "mogul_angles_RMSZ": {
            "type": "number",
            "description": "The root-mean-square value of the Z-scores of bond angles for the non-polymer instance in degrees\nobtained from a CCDC Mogul survey of bond angles in the CSD small molecule crystal structure database.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "mogul_bond_outliers": {
            "type": "integer",
            "description": "Number of bond distance outliers obtained from a CCDC Mogul survey of bond lengths in the CSD small\n   molecule crystal structure database.  Outliers are defined as bond distances that have a Z-score\n   less than -2 or greater than 2.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "mogul_bonds_RMSZ": {
            "type": "number",
            "description": "The root-mean-square value of the Z-scores of bond lengths for the nonpolymer instance in Angstroms\nobtained from a CCDC Mogul survey of bond lengths in the CSD small molecule crystal structure database.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "ranking_model_fit": {
            "type": "number",
            "description": "The ranking of the model fit score component.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "ranking_model_geometry": {
            "type": "number",
            "description": "The ranking of the model geometry score component.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "stereo_outliers": {
            "type": "integer",
            "description": "Number of stereochemical/chirality errors.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_target_neighbors": {
        "distance": {
            "type": "number",
            "description": "Distance value for this target interaction.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "target_asym_id": {
            "type": "string",
            "description": "The entity instance identifier for the target of interaction.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "target_comp_id": {
            "type": "string",
            "description": "The chemical component identifier for the target of interaction.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "target_entity_id": {
            "type": "string",
            "description": "The entity identifier for the target of interaction.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "target_is_bound": {
            "type": "string",
            "description": "A flag to indicate the nature of the target interaction is covalent or metal-coordination.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_uniprot_container_identifiers": {
        "reference_sequence_identifiers": {
            "database_accession": {
                "type": "string",
                "description": "Reference database accession code",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "database_isoform": {
                "type": "string",
                "description": "Reference database identifier for the sequence isoform",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "database_name": {
                "type": "string",
                "description": "Reference database name",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_uniprot_protein": {
        "name": {
            "value": {
                "type": "string",
                "description": "Name that allows to unambiguously identify a protein.",
                "search": [
                    "exact-match",
                    "full-text",
                    "suggest"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_uniprot_annotation": {
        "annotation_id": {
            "type": "string",
            "description": "An identifier for the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "A description for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "A type or category of the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "annotation_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the annotation lineage as parent lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class identifiers.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class names.",
                "search": [
                    "exact-match",
                    "full-text"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_uniprot_external_reference": {
        "reference_name": {
            "type": "string",
            "description": "",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_branched_entity_instance_container_identifiers": {
        "asym_id": {
            "type": "string",
            "description": "Instance identifier for this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "auth_asym_id": {
            "type": "string",
            "description": "Author instance identifier for this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entity_id": {
            "type": "string",
            "description": "Entity identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entry_id": {
            "type": "string",
            "description": "Entry identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_id": {
            "type": "string",
            "description": "A unique identifier for each object in this entity instance container formed by\n an 'dot' (.) separated concatenation of entry and entity instance identifiers.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_branched_instance_annotation": {
        "annotation_id": {
            "type": "string",
            "description": "An identifier for the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "A description for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "A type or category of the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "annotation_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the annotation lineage as parent lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class identifiers.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class names.",
                "search": [
                    "exact-match",
                    "full-text"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_branched_instance_feature_summary": {
        "count": {
            "type": "integer",
            "description": "The feature count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "coverage": {
            "type": "number",
            "description": "The fractional feature coverage relative to the full branched entity.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "maximum_length": {
            "type": "integer",
            "description": "The maximum feature length.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "minimum_length": {
            "type": "integer",
            "description": "The minimum feature length.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "Type or category of the feature.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_ligand_neighbors": {
        "distance": {
            "type": "number",
            "description": "Distance value for this ligand interaction.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "ligand_asym_id": {
            "type": "string",
            "description": "The entity instance identifier for the ligand interaction.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "ligand_comp_id": {
            "type": "string",
            "description": "The chemical component identifier for the ligand interaction.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "ligand_entity_id": {
            "type": "string",
            "description": "The entity identifier for the ligand of interaction.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "ligand_is_bound": {
            "type": "string",
            "description": "A flag to indicate the nature of the ligand interaction is covalent or metal-coordination.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_entity_branch": {
        "rcsb_branched_component_count": {
            "type": "integer",
            "description": "Number of constituent chemical components in the branched entity.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "The type of this branched oligosaccharide.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_entity_branch_descriptor": {
        "descriptor": {
            "type": "string",
            "description": "This data item contains the descriptor value for this\n entity.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "This data item contains the descriptor type.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_branched_entity": {
        "details": {
            "type": "string",
            "description": "A description of special aspects of the branched entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "formula_weight": {
            "type": "number",
            "description": "Formula mass (KDa) of the branched entity.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "pdbx_description": {
            "type": "string",
            "description": "A description of the branched entity.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_number_of_molecules": {
            "type": "integer",
            "description": "The number of molecules of the branched entity in the entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_branched_entity_annotation": {
        "annotation_id": {
            "type": "string",
            "description": "An identifier for the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "A description for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "A type or category of the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "annotation_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the annotation lineage as parent lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class identifiers.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class names.",
                "search": [
                    "exact-match",
                    "full-text"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_branched_entity_container_identifiers": {
        "chem_comp_monomers": {
            "type": "string",
            "description": "Unique list of monomer chemical component identifiers in the entity in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "chem_ref_def_id": {
            "type": "string",
            "description": "The chemical reference definition identifier for the entity in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entity_id": {
            "type": "string",
            "description": "Entity identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entry_id": {
            "type": "string",
            "description": "Entry identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "prd_id": {
            "type": "string",
            "description": "The BIRD identifier for the entity in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_id": {
            "type": "string",
            "description": "A unique identifier for each object in this entity container formed by\n an underscore separated concatenation of entry and entity identifiers.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "reference_identifiers": {
            "resource_accession": {
                "type": "string",
                "description": "Reference resource accession code",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "resource_name": {
                "type": "string",
                "description": "Reference resource name",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_branched_entity_feature_summary": {
        "count": {
            "type": "integer",
            "description": "The feature count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "coverage": {
            "type": "number",
            "description": "The fractional feature coverage relative to the full branched entity.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "maximum_length": {
            "type": "integer",
            "description": "The maximum feature length.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "minimum_length": {
            "type": "integer",
            "description": "The minimum feature length.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "Type or category of the feature.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_branched_entity_keywords": {
        "text": {
            "type": "string",
            "description": "Keywords describing this branched entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_branched_entity_name_com": {
        "name": {
            "type": "string",
            "description": "A common name for the branched entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_branched_entity_name_sys": {
        "name": {
            "type": "string",
            "description": "The systematic name for the branched entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_polymer_entity_instance_container_identifiers": {
        "asym_id": {
            "type": "string",
            "description": "Instance identifier for this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "auth_asym_id": {
            "type": "string",
            "description": "Author instance identifier for this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entity_id": {
            "type": "string",
            "description": "Entity identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entry_id": {
            "type": "string",
            "description": "Entry identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_id": {
            "type": "string",
            "description": "A unique identifier for each object in this entity instance container formed by\n an 'dot' (.) separated concatenation of entry and entity instance identifiers.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_polymer_instance_annotation": {
        "annotation_id": {
            "type": "string",
            "description": "An identifier for the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "A description for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "A type or category of the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "annotation_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the annotation lineage as parent lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class identifiers.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class names.",
                "search": [
                    "exact-match",
                    "full-text"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_polymer_instance_feature_summary": {
        "count": {
            "type": "integer",
            "description": "The feature count per polymer chain.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "coverage": {
            "type": "number",
            "description": "The fractional feature coverage relative to the full entity sequence.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "maximum_length": {
            "type": "integer",
            "description": "The maximum feature length.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "minimum_length": {
            "type": "integer",
            "description": "The minimum feature length.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "Type or category of the feature.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_polymer_struct_conn": {
        "connect_type": {
            "type": "string",
            "description": "The connection type.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "role": {
            "type": "string",
            "description": "The chemical or structural role of the interaction",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        },
        "value_order": {
            "type": "string",
            "description": "The chemical bond order associated with the specified atoms in\n this contact.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "audit_author": {
        "identifier_ORCID": {
            "type": "string",
            "description": "The Open Researcher and Contributor ID (ORCID).",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "The name of an author of this data block. If there are multiple\n authors, _audit_author.name is looped with _audit_author.address.\n The family name(s), followed by a comma and including any\n dynastic components, precedes the first name(s) or initial(s).",
            "search": [
                "exact-match",
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        }
    },
    "cell": {
        "angle_alpha": {
            "type": "number",
            "description": "Unit-cell angle alpha of the reported structure in degrees.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "angle_beta": {
            "type": "number",
            "description": "Unit-cell angle beta of the reported structure in degrees.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "angle_gamma": {
            "type": "number",
            "description": "Unit-cell angle gamma of the reported structure in degrees.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "length_a": {
            "type": "number",
            "description": "Unit-cell length a corresponding to the structure reported in\nangstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "length_b": {
            "type": "number",
            "description": "Unit-cell length b corresponding to the structure reported in\n angstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "length_c": {
            "type": "number",
            "description": "Unit-cell length c corresponding to the structure reported in\nangstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "citation": {
        "book_title": {
            "type": "string",
            "description": "The title of the book in which the citation appeared; relevant\n for books or book chapters.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "id": {
            "type": "string",
            "description": "The value of _citation.id must uniquely identify a record in the\n CITATION list.\n\n The _citation.id 'primary' should be used to indicate the\n citation that the author(s) consider to be the most pertinent to\n the contents of the data block.\n\n Note that this item need not be a number; it can be any unique\n identifier.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "journal_abbrev": {
            "type": "string",
            "description": "Abbreviated name of the cited journal as given in the\n Chemical Abstracts Service Source Index.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "journal_id_ASTM": {
            "type": "string",
            "description": "The American Society for Testing and Materials (ASTM) code\n assigned to the journal cited (also referred to as the CODEN\n designator of the Chemical Abstracts Service); relevant for\n journal articles.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "journal_id_ISSN": {
            "type": "string",
            "description": "The International Standard Serial Number (ISSN) code assigned to\n the journal cited; relevant for journal articles.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "pdbx_database_id_DOI": {
            "type": "string",
            "description": "Document Object Identifier used by doi.org to uniquely\n specify bibliographic entry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_authors": {
            "type": "string",
            "description": "Names of the authors of the citation; relevant for journal\n articles, books and book chapters.  Names are separated by vertical bars.\n\n The family name(s), followed by a comma and including any\n dynastic components, precedes the first name(s) or initial(s).",
            "search": [
                "exact-match",
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        },
        "rcsb_is_primary": {
            "type": "string",
            "description": "Flag to indicate a primary citation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_journal_abbrev": {
            "type": "string",
            "description": "Normalized journal abbreviation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "title": {
            "type": "string",
            "description": "The title of the citation; relevant for journal articles, books\n and book chapters.",
            "search": [
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        },
        "unpublished_flag": {
            "type": "string",
            "description": "Flag to indicate that this citation will not be published.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "year": {
            "type": "integer",
            "description": "The year of the citation; relevant for journal articles, books\n and book chapters.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "database_2": {
        "database_code": {
            "type": "string",
            "description": "The code assigned by the database identified in\n _database_2.database_id.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "pdbx_database_accession": {
            "type": "string",
            "description": "Extended accession code issued for for _database_2.database_code assigned by the database identified in\n _database_2.database_id.",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        }
    },
    "diffrn": {
        "ambient_pressure": {
            "type": "number",
            "description": "The mean hydrostatic pressure in kilopascals at which the\n intensities were measured.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "ambient_temp": {
            "type": "number",
            "description": "The mean temperature in kelvins at which the intensities were\n measured.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "crystal_support": {
            "type": "string",
            "description": "The physical device used to support the crystal during data\n collection.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "details": {
            "type": "string",
            "description": "Special details of the diffraction measurement process. Should\n include information about source instability, crystal motion,\n degradation and so on.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_serial_crystal_experiment": {
            "type": "string",
            "description": "Y/N if using serial crystallography experiment in which multiple crystals contribute to each diffraction frame in the experiment.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "diffrn_detector": {
        "details": {
            "type": "string",
            "description": "A description of special aspects of the radiation detector.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "detector": {
            "type": "string",
            "description": "The general class of the radiation detector.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_collection_date": {
            "type": "string",
            "description": "The date of data collection.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "The make, model or name of the detector device used.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "diffrn_radiation": {
        "collimation": {
            "type": "string",
            "description": "The collimation or focusing applied to the radiation.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "monochromator": {
            "type": "string",
            "description": "The method used to obtain monochromatic radiation. If a mono-\n chromator crystal is used, the material and the indices of the\n Bragg reflection are specified.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_diffrn_protocol": {
            "type": "string",
            "description": "SINGLE WAVELENGTH, LAUE, or MAD.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "diffrn_source": {
        "details": {
            "type": "string",
            "description": "A description of special aspects of the radiation source used.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_synchrotron_beamline": {
            "type": "string",
            "description": "Synchrotron beamline.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "pdbx_synchrotron_site": {
            "type": "string",
            "description": "Synchrotron site.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "source": {
            "type": "string",
            "description": "The general class of the radiation source.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "The make, model or name of the source of radiation.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "em_2d_crystal_entity": {
        "angle_gamma": {
            "type": "number",
            "description": "Unit-cell angle gamma in degrees.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "c_sampling_length": {
            "type": "number",
            "description": "Length used to sample the reciprocal lattice lines in the c-direction.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "length_a": {
            "type": "number",
            "description": "Unit-cell length a in angstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "length_b": {
            "type": "number",
            "description": "Unit-cell length b in angstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "length_c": {
            "type": "number",
            "description": "Thickness of 2D crystal",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "em_3d_crystal_entity": {
        "angle_alpha": {
            "type": "number",
            "description": "Unit-cell angle alpha in degrees.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "angle_beta": {
            "type": "number",
            "description": "Unit-cell angle beta in degrees.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "angle_gamma": {
            "type": "number",
            "description": "Unit-cell angle gamma in degrees.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "length_a": {
            "type": "number",
            "description": "Unit-cell length a in angstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "length_b": {
            "type": "number",
            "description": "Unit-cell length b in angstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "length_c": {
            "type": "number",
            "description": "Unit-cell length c in angstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "space_group_name": {
            "type": "string",
            "description": "Space group name.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "space_group_num": {
            "type": "integer",
            "description": "Space group number.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "em_3d_fitting": {
        "details": {
            "type": "string",
            "description": "Any additional details regarding fitting of atomic coordinates into\n the 3DEM volume, including data and considerations from other\n methods used in computation of the model.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "method": {
            "type": "string",
            "description": "The method used to fit atomic coordinates\n into the 3dem reconstructed map.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "overall_b_value": {
            "type": "number",
            "description": "The overall B (temperature factor) value for the 3d-em volume.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "ref_protocol": {
            "type": "string",
            "description": "The refinement protocol used.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "ref_space": {
            "type": "string",
            "description": "A flag to indicate whether fitting was carried out in real\n or reciprocal refinement space.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "target_criteria": {
            "type": "string",
            "description": "The measure used to assess quality of fit of the atomic coordinates in the\n 3DEM map volume.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "em_3d_fitting_list": {
        "details": {
            "type": "string",
            "description": "Details about the model used in fitting.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "em_3d_reconstruction": {
        "actual_pixel_size": {
            "type": "number",
            "description": "The actual pixel size of the projection set of images in Angstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "algorithm": {
            "type": "string",
            "description": "The reconstruction algorithm/technique used to generate the map.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "method": {
            "type": "string",
            "description": "The algorithm method used for the 3d-reconstruction.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "nominal_pixel_size": {
            "type": "number",
            "description": "The nominal pixel size of the projection set of images in Angstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "num_class_averages": {
            "type": "integer",
            "description": "The number of classes used in the final 3d reconstruction",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "num_particles": {
            "type": "integer",
            "description": "The number of 2D projections or 3D subtomograms used in the 3d reconstruction",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "refinement_type": {
            "type": "string",
            "description": "Indicates details on how the half-map used for resolution determination (usually by FSC) have been generated.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "resolution": {
            "type": "number",
            "description": "The final resolution (in angstroms) of the 3D reconstruction.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "resolution_method": {
            "type": "string",
            "description": "The  method used to determine the final resolution\n of the 3d reconstruction.\n The Fourier Shell Correlation criterion as a measure of\n resolution is based on the concept of splitting the (2D)\n data set into two halves; averaging each and comparing them\n using the Fourier Ring Correlation (FRC) technique.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "symmetry_type": {
            "type": "string",
            "description": "The type of symmetry applied to the reconstruction",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "em_ctf_correction": {
        "details": {
            "type": "string",
            "description": "Any additional details about CTF correction",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "Type of CTF correction applied",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "em_diffraction": {
        "camera_length": {
            "type": "number",
            "description": "The camera length (in millimeters). The camera length is the\n product of the objective focal length and the combined magnification\n of the intermediate and projector lenses when the microscope is\n operated in the diffraction mode.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "em_diffraction_shell": {
        "fourier_space_coverage": {
            "type": "number",
            "description": "Completeness of the structure factor data within this resolution shell, in percent",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "high_resolution": {
            "type": "number",
            "description": "High resolution limit for this shell (angstroms)",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "low_resolution": {
            "type": "number",
            "description": "Low resolution limit for this shell (angstroms)",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "multiplicity": {
            "type": "number",
            "description": "Multiplicity (average number of measurements) for the structure factors in this resolution shell",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "num_structure_factors": {
            "type": "integer",
            "description": "Number of measured structure factors in this resolution shell",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "phase_residual": {
            "type": "number",
            "description": "Phase residual for this resolution shell, in degrees",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "em_diffraction_stats": {
        "fourier_space_coverage": {
            "type": "number",
            "description": "Completeness of the structure factor data within the defined space group\n at the reported resolution (percent).",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "high_resolution": {
            "type": "number",
            "description": "High resolution limit of the structure factor data, in angstroms",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "num_intensities_measured": {
            "type": "integer",
            "description": "Total number of diffraction intensities measured (before averaging)",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "num_structure_factors": {
            "type": "integer",
            "description": "Number of structure factors obtained (merged amplitudes + phases)",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "overall_phase_error": {
            "type": "number",
            "description": "Overall phase error in degrees",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "overall_phase_residual": {
            "type": "number",
            "description": "Overall phase residual in degrees",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "r_merge": {
            "type": "number",
            "description": "Rmerge value (percent)",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "r_sym": {
            "type": "number",
            "description": "Rsym value (percent)",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "em_embedding": {
        "details": {
            "type": "string",
            "description": "Staining procedure used in the specimen preparation.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "material": {
            "type": "string",
            "description": "The embedding  material.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "em_entity_assembly": {
        "parent_id": {
            "type": "integer",
            "description": "The parent of this assembly.\n This data item is an internal category pointer to _em_entity_assembly.id.\n By convention, the full assembly (top of hierarchy) is assigned parent id 0 (zero).",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "source": {
            "type": "string",
            "description": "The type of source (e.g., natural source) for the component (sample or sample\nsubcomponent)",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "em_experiment": {
        "aggregation_state": {
            "type": "string",
            "description": "The aggregation/assembly state of the imaged specimen.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "reconstruction_method": {
            "type": "string",
            "description": "The reconstruction method used in the EM experiment.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "em_helical_entity": {
        "angular_rotation_per_subunit": {
            "type": "number",
            "description": "The angular rotation per helical subunit in degrees. Negative values indicate left-handed helices; positive values indicate right handed helices.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "axial_rise_per_subunit": {
            "type": "number",
            "description": "The axial rise per subunit in the helical assembly.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "axial_symmetry": {
            "type": "string",
            "description": "Symmetry of the helical axis, either cyclic (Cn) or dihedral (Dn), where n>=1.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "em_image_recording": {
        "average_exposure_time": {
            "type": "number",
            "description": "The average exposure time for each image.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "avg_electron_dose_per_image": {
            "type": "number",
            "description": "The electron dose received by the specimen per image (electrons per square angstrom).",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "detector_mode": {
            "type": "string",
            "description": "The detector mode used during image recording.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "film_or_detector_model": {
            "type": "string",
            "description": "The detector type used for recording images.\n Usually film , CCD camera or direct electron detector.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "num_diffraction_images": {
            "type": "integer",
            "description": "The number of diffraction images collected.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "num_grids_imaged": {
            "type": "integer",
            "description": "Number of grids in the microscopy session",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "num_real_images": {
            "type": "integer",
            "description": "The number of micrograph images collected.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "em_imaging": {
        "accelerating_voltage": {
            "type": "integer",
            "description": "A value of accelerating voltage (in kV) used for imaging.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "alignment_procedure": {
            "type": "string",
            "description": "The type of procedure used to align the microscope electron beam.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "c2_aperture_diameter": {
            "type": "number",
            "description": "The open diameter of the c2 condenser lens,\n in microns.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "calibrated_defocus_max": {
            "type": "number",
            "description": "The maximum calibrated defocus value of the objective lens (in nanometers) used\n to obtain the recorded images. Negative values refer to overfocus.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "calibrated_defocus_min": {
            "type": "number",
            "description": "The minimum calibrated defocus value of the objective lens (in nanometers) used\n to obtain the recorded images. Negative values refer to overfocus.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "calibrated_magnification": {
            "type": "integer",
            "description": "The magnification value obtained for a known standard just\n prior to, during or just after the imaging experiment.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "cryogen": {
            "type": "string",
            "description": "Cryogen type used to maintain the specimen stage temperature during imaging\n in the microscope.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "date": {
            "type": "string",
            "description": "Date (YYYY-MM-DD) of imaging experiment or the date at which\n a series of experiments began.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "detector_distance": {
            "type": "number",
            "description": "The camera length (in millimeters). The camera length is the\n product of the objective focal length and the combined magnification\n of the intermediate and projector lenses when the microscope is\n operated in the diffraction mode.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "illumination_mode": {
            "type": "string",
            "description": "The mode of illumination.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "microscope_model": {
            "type": "string",
            "description": "The name of the model of microscope.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "mode": {
            "type": "string",
            "description": "The mode of imaging.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "nominal_cs": {
            "type": "number",
            "description": "The spherical aberration coefficient (Cs) in millimeters,\n of the objective lens.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "nominal_defocus_max": {
            "type": "number",
            "description": "The maximum defocus value of the objective lens (in nanometers) used\n to obtain the recorded images. Negative values refer to overfocus.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "nominal_defocus_min": {
            "type": "number",
            "description": "The minimum defocus value of the objective lens (in nanometers) used\n to obtain the recorded images. Negative values refer to overfocus.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "nominal_magnification": {
            "type": "integer",
            "description": "The magnification indicated by the microscope readout.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "recording_temperature_maximum": {
            "type": "number",
            "description": "The specimen temperature maximum (kelvin) for the duration\n of imaging.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "recording_temperature_minimum": {
            "type": "number",
            "description": "The specimen temperature minimum (kelvin) for the duration\n of imaging.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "residual_tilt": {
            "type": "number",
            "description": "Residual tilt of the electron beam (in miliradians)",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "specimen_holder_model": {
            "type": "string",
            "description": "The name of the model of specimen holder used during imaging.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "temperature": {
            "type": "number",
            "description": "The mean specimen stage temperature (in kelvin) during imaging\n in the microscope.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "tilt_angle_max": {
            "type": "number",
            "description": "The maximum angle at which the specimen was tilted to obtain\n recorded images.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "tilt_angle_min": {
            "type": "number",
            "description": "The minimum angle at which the specimen was tilted to obtain\n recorded images.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "em_particle_selection": {
        "num_particles_selected": {
            "type": "integer",
            "description": "The number of particles selected from the projection set of images.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "em_single_particle_entity": {
        "point_symmetry": {
            "type": "string",
            "description": "Point symmetry symbol, either Cn, Dn, T, O, or I",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "em_software": {
        "category": {
            "type": "string",
            "description": "The purpose of the software.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "The name of the software package used, e.g., RELION.  Depositors are strongly\n  encouraged to provide a value in this field.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "em_specimen": {
        "concentration": {
            "type": "number",
            "description": "The concentration (in milligrams per milliliter, mg/ml)\n of the complex in the sample.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "shadowing_applied": {
            "type": "string",
            "description": "'YES' indicates that the specimen has been shadowed.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "staining_applied": {
            "type": "string",
            "description": "'YES' indicates that the specimen has been stained.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "vitrification_applied": {
            "type": "string",
            "description": "'YES' indicates that the specimen was vitrified by cryopreservation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "em_staining": {
        "details": {
            "type": "string",
            "description": "Staining procedure used in the specimen preparation.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "material": {
            "type": "string",
            "description": "The staining  material.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "type of staining",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "em_vitrification": {
        "chamber_temperature": {
            "type": "number",
            "description": "The temperature (in kelvin) of the sample just prior to vitrification.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "cryogen_name": {
            "type": "string",
            "description": "This is the name of the cryogen.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "humidity": {
            "type": "number",
            "description": "Relative humidity (%) of air surrounding the specimen just prior to\nvitrification.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "instrument": {
            "type": "string",
            "description": "The type of instrument used in the vitrification process.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "method": {
            "type": "string",
            "description": "The procedure for vitrification.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "temp": {
            "type": "number",
            "description": "The vitrification temperature (in kelvin), e.g.,\n  temperature of the plunge instrument cryogen bath.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "exptl": {
        "crystals_number": {
            "type": "integer",
            "description": "The total number of crystals used in the  measurement of\n intensities.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "details": {
            "type": "string",
            "description": "Any special information about the experimental work prior to the\n intensity measurement. See also _exptl_crystal.preparation.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "method": {
            "type": "string",
            "description": "The method used in the experiment.",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        }
    },
    "exptl_crystal": {
        "density_Matthews": {
            "type": "number",
            "description": "The density of the crystal, expressed as the ratio of the\n volume of the asymmetric unit to the molecular mass of a\n monomer of the structure, in units of angstroms^3^ per dalton.\n\n Ref: Matthews, B. W. (1968). J. Mol. Biol. 33, 491-497.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "density_meas": {
            "type": "number",
            "description": "Density values measured using standard chemical and physical\n methods. The units are megagrams per cubic metre (grams per\n cubic centimetre).",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "density_percent_sol": {
            "type": "number",
            "description": "Density value P calculated from the crystal cell and contents,\n expressed as per cent solvent.\n\n P = 1 - (1.23 N MMass) / V\n\n N     = the number of molecules in the unit cell\n MMass = the molecular mass of each molecule (gm/mole)\n V     = the volume of the unit cell (A^3^)\n 1.23  = a conversion factor evaluated as:\n\n         (0.74 cm^3^/g) (10^24^ A^3^/cm^3^)\n         --------------------------------------\n              (6.02*10^23^) molecules/mole\n\n         where 0.74 is an assumed value for the partial specific\n         volume of the molecule",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "pdbx_mosaicity": {
            "type": "number",
            "description": "Isotropic approximation of the distribution of mis-orientation angles\nspecified in degrees of all the mosaic domain blocks in the crystal,\nrepresented as a standard deviation. Here, a mosaic block is a set of\ncontiguous unit cells assumed to be perfectly aligned. Lower mosaicity\nindicates better ordered crystals. See for example:\n\nNave, C. (1998). Acta Cryst. D54, 848-853.\n\nNote that many software packages estimate the mosaic rotation distribution\ndifferently and may combine several physical properties of the experiment\ninto a single mosaic term. This term will help fit the modeled spots\nto the observed spots without necessarily being directly related to the\nphysics of the crystal itself.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "pdbx_mosaicity_esd": {
            "type": "number",
            "description": "The uncertainty in the mosaicity estimate for the crystal.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "exptl_crystal_grow": {
        "method": {
            "type": "string",
            "description": "The method used to grow the crystals.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pH": {
            "type": "number",
            "description": "The pH at which the crystal was grown. If more than one pH was\n employed during the crystallization process, the final pH should\n be noted here and the protocol involving multiple pH values\n should be described in _exptl_crystal_grow.details.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "pdbx_details": {
            "type": "string",
            "description": "Text description of crystal growth procedure.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "temp": {
            "type": "number",
            "description": "The temperature in kelvins at which the crystal was grown.\n If more than one temperature was employed during the\n crystallization process, the final temperature should be noted\n here and the protocol  involving multiple temperatures should be\n described in _exptl_crystal_grow.details.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "ihm_entry_collection_mapping": {
        "collection_id": {
            "type": "string",
            "description": "Identifier for the entry collection. \n This data item is a pointer to _ihm_entry_collection.id in the \n IHM_ENTRY_COLLECTION category.",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        }
    },
    "pdbx_SG_project": {
        "full_name_of_center": {
            "type": "string",
            "description": "The value identifies the full name of center.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "initial_of_center": {
            "type": "string",
            "description": "The value identifies the full name of center.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "project_name": {
            "type": "string",
            "description": "The value identifies the Structural Genomics project.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_audit_support": {
        "country": {
            "type": "string",
            "description": "The country/region providing the funding support for the entry.\n Funding information is optionally provided for entries after June 2016.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "funding_organization": {
            "type": "string",
            "description": "The name of the organization providing funding support for the\n entry. Funding information is optionally provided for entries\n after June 2016.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "grant_number": {
            "type": "string",
            "description": "The grant number associated with this source of support.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_database_PDB_obs_spr": {
        "replace_pdb_id": {
            "type": "string",
            "description": "The PDB identifier for the replaced (OLD) entry/entries.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_database_related": {
        "content_type": {
            "type": "string",
            "description": "The identifying content type of the related entry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "db_id": {
            "type": "string",
            "description": "The identifying code in the related database.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "db_name": {
            "type": "string",
            "description": "The name of the database containing the related entry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_database_status": {
        "pdb_format_compatible": {
            "type": "string",
            "description": "A flag indicating that the entry is compatible with the PDB format.\n\n A value of 'N' indicates that the no PDB format data file is\n corresponding to this entry is available in the PDB archive.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_deposit_group": {
        "group_description": {
            "type": "string",
            "description": "A description of the contents of entries in the collection.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "group_id": {
            "type": "string",
            "description": "A unique identifier for a group of entries deposited as a collection.",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        },
        "group_title": {
            "type": "string",
            "description": "A title to describe the group of entries deposited in the collection.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "group_type": {
            "type": "string",
            "description": "Text to describe a grouping of entries in multiple collections",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_initial_refinement_model": {
        "accession_code": {
            "type": "string",
            "description": "This item identifies an accession code of the resource where the initial model\n is used",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "source_name": {
            "type": "string",
            "description": "This item identifies the resource of initial model used for refinement",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "This item describes the type of the initial model was generated",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_molecule_features": {
        "class": {
            "type": "string",
            "description": "Broadly defines the function of the molecule.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "details": {
            "type": "string",
            "description": "Additional details describing the molecule.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name of the molecule.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "prd_id": {
            "type": "string",
            "description": "The value of _pdbx_molecule_features.prd_id is the accession code for this\n reference molecule.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_nmr_details": {
        "text": {
            "type": "string",
            "description": "Additional details describing the NMR experiment.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_nmr_refine": {
        "details": {
            "type": "string",
            "description": "Additional details about the NMR refinement.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "method": {
            "type": "string",
            "description": "The method used to determine the structure.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_nmr_sample_details": {
        "contents": {
            "type": "string",
            "description": "A complete description of each NMR sample. Include the concentration\nand concentration units for each component (include buffers, etc.). For each\ncomponent describe the isotopic composition, including the % labeling level,\nif known.\n\nFor example:\n1. Uniform (random) labeling with 15N: U-15N\n2. Uniform (random) labeling with 13C, 15N at known labeling\n   levels: U-95% 13C;U-98% 15N\n3. Residue selective labeling: U-95% 15N-Thymine\n4. Site specific labeling: 95% 13C-Ala18,\n5. Natural abundance labeling in an otherwise uniformly labeled\n   biomolecule is designated by NA: U-13C; NA-K,H",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "details": {
            "type": "string",
            "description": "Brief description of the sample providing additional information not captured by other items in the category.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "label": {
            "type": "string",
            "description": "A value that uniquely identifies this sample from the other samples listed\nin the entry.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_nmr_software": {
        "name": {
            "type": "string",
            "description": "The name of the software used for the task.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_nmr_spectrometer": {
        "field_strength": {
            "type": "number",
            "description": "The field strength in MHz of the spectrometer",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "manufacturer": {
            "type": "string",
            "description": "The name of the manufacturer of the spectrometer.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "model": {
            "type": "string",
            "description": "The model of the NMR spectrometer.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_reflns_twin": {
        "type": {
            "type": "string",
            "description": "There are two types of twinning: merohedral or hemihedral\n                                 non-merohedral or epitaxial\n\nFor merohedral twinning the diffraction patterns from the different domains are\ncompletely superimposable.   Hemihedral twinning is a special case of merohedral\ntwinning. It only involves two distinct domains.  Pseudo-merohedral twinning is\na subclass merohedral twinning in which lattice is coincidentally superimposable.\n\nIn the case of non-merohedral or epitaxial twinning  the reciprocal\nlattices do not superimpose exactly. In this case the  diffraction pattern\nconsists of two (or more) interpenetrating lattices, which can in principle\nbe separated.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_serial_crystallography_measurement": {
        "collimation": {
            "type": "string",
            "description": "The collimation or type of focusing optics applied to the radiation.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_serial_crystallography_sample_delivery": {
        "description": {
            "type": "string",
            "description": "The description of the mechanism by which the specimen in placed in the path\n of the source.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "method": {
            "type": "string",
            "description": "The description of the mechanism by which the specimen in placed in the path\n of the source.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_serial_crystallography_sample_delivery_fixed_target": {
        "description": {
            "type": "string",
            "description": "For a fixed target sample, a description of sample preparation",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "details": {
            "type": "string",
            "description": "Any details pertinent to the fixed sample target",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_serial_crystallography_sample_delivery_injection": {
        "description": {
            "type": "string",
            "description": "For continuous sample flow experiments, a description of the injector used\n to move the sample into the beam.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "injector_nozzle": {
            "type": "string",
            "description": "The type of nozzle to deliver and focus sample jet",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "preparation": {
            "type": "string",
            "description": "Details of crystal growth and preparation of the crystals",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_soln_scatter": {
        "data_analysis_software_list": {
            "type": "string",
            "description": "A list of the software used in the data analysis",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "data_reduction_software_list": {
            "type": "string",
            "description": "A list of the software used in the data reduction",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "detector_specific": {
            "type": "string",
            "description": "The particular radiation detector. In general this will be a\n  manufacturer, description, model number or some combination of\n  these.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "detector_type": {
            "type": "string",
            "description": "The general class of the radiation detector.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "source_beamline": {
            "type": "string",
            "description": "The beamline name used for the experiment",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "source_beamline_instrument": {
            "type": "string",
            "description": "The instrumentation used on the beamline",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "source_class": {
            "type": "string",
            "description": "The general class of the radiation source.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "source_type": {
            "type": "string",
            "description": "The make, model, name or beamline of the source of radiation.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_soln_scatter_model": {
        "conformer_selection_criteria": {
            "type": "string",
            "description": "A description of the conformer selection criteria\n used.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "details": {
            "type": "string",
            "description": "A description of any additional details concerning the experiment.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "method": {
            "type": "string",
            "description": "A description of the methods used in the modelling",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "software_list": {
            "type": "string",
            "description": "A list of the software used in the modeeling",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_vrpt_summary_geometry": {
        "angles_RMSZ": {
            "type": "number",
            "description": "The overall root mean square of the Z-score for deviations of bond angles in comparison to \n\"standard geometry\" made using the MolProbity dangle program.\nStandard geometry parameters are taken from Engh and Huber (2001) and Parkinson et al. (1996).\nThis value is for all chains in the structure.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "bonds_RMSZ": {
            "type": "number",
            "description": "The overall root mean square of the Z-score for deviations of bond lengths in comparison to \n\"standard geometry\" made using the MolProbity dangle program.\nStandard geometry parameters are taken from Engh and Huber (2001) and Parkinson et al. (1996).\nThis value is for all chains in the structure.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "clashscore": {
            "type": "number",
            "description": "This score is derived from the number of pairs of atoms in the PDB_model_num that are unusually close to each other. \nIt is calculated by the MolProbity pdbx_vrpt_software and expressed as the number or such clashes per thousand atoms.\nFor structures determined by NMR the clashscore value here will only consider label_atom_id pairs in the \nwell-defined (core) residues from ensemble analysis.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "percent_ramachandran_outliers": {
            "type": "number",
            "description": "The percentage of residues with Ramachandran outliers.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "percent_rotamer_outliers": {
            "type": "number",
            "description": "The MolProbity sidechain outlier score (a percentage).\nProtein sidechains mostly adopt certain (combinations of) preferred torsion angle values \n(called rotamers or rotameric conformers), much like their backbone torsion angles \n(as assessed in the Ramachandran analysis). MolProbity considers the sidechain conformation \nof a residue to be an outlier if its set of torsion angles is not similar to any preferred \ncombination. The sidechain outlier score is calculated as the percentage of residues \nwith an unusual sidechain conformation with respect to the total number of residues for \nwhich the assessment is available.\nExample: percent-rota-outliers=\"2.44\".\nSpecific to structure that contain protein chains and have sidechains modelled.\nFor NMR structures only the  well-defined (core) residues from ensemble analysis will be considered.\nThe percentage of residues with rotamer outliers.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_accession_info": {
        "deposit_date": {
            "type": "string",
            "description": "The entry deposition date.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "has_released_experimental_data": {
            "type": "string",
            "description": "A code indicating the current availibility of experimental data in the repository.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "initial_release_date": {
            "type": "string",
            "description": "The entry initial release date.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "revision_date": {
            "type": "string",
            "description": "The latest entry revision date.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_binding_affinity": {
        "comp_id": {
            "type": "string",
            "description": "Ligand identifier.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "Binding affinity measurement given in one of the following types:  The concentration constants: IC50: the concentration of ligand that reduces enzyme activity by 50%;  EC50: the concentration of compound that generates a half-maximal response;  The binding constant:  Kd: dissociation constant;  Ka: association constant;  Ki: enzyme inhibition constant;  The thermodynamic parameters:  delta G: Gibbs free energy of binding (for association reaction);  delta H: change in enthalpy associated with a chemical reaction;  delta S: change in entropy associated with a chemical reaction.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "value": {
            "type": "number",
            "description": "Binding affinity value between a ligand and its target molecule.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_comp_model_provenance": {
        "entry_id": {
            "type": "string",
            "description": "Entry identifier corresponding to the computed structure model.",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        },
        "source_db": {
            "type": "string",
            "description": "Source database for the computed structure model.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_entry_container_identifiers": {
        "emdb_ids": {
            "type": "string",
            "description": "List of EMDB identifiers for the 3D electron microscopy density maps\n used in the production of the structure model.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entry_id": {
            "type": "string",
            "description": "Entry identifier for the container.",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        },
        "rcsb_id": {
            "type": "string",
            "description": "A unique identifier for each object in this entry container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "related_emdb_ids": {
            "type": "string",
            "description": "List of EMDB identifiers for the 3D electron microscopy density maps\n related to the structure model.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_entry_group_membership": {
        "aggregation_method": {
            "type": "string",
            "description": "Method used to establish group membership",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "group_id": {
            "type": "string",
            "description": "A unique identifier for a group of entries",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_entry_info": {
        "assembly_count": {
            "type": "integer",
            "description": "The number of assemblies defined for this entry including the deposited assembly.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "branched_entity_count": {
            "type": "integer",
            "description": "The number of distinct branched entities in the structure entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "cis_peptide_count": {
            "type": "integer",
            "description": "The number of cis-peptide linkages per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deposited_atom_count": {
            "type": "integer",
            "description": "The number of heavy atom coordinates records per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deposited_deuterated_water_count": {
            "type": "integer",
            "description": "The number of deuterated water molecules per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deposited_hydrogen_atom_count": {
            "type": "integer",
            "description": "The number of hydrogen atom coordinates records per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deposited_model_count": {
            "type": "integer",
            "description": "The number of model structures deposited.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deposited_modeled_polymer_monomer_count": {
            "type": "integer",
            "description": "The number of modeled polymer monomers in the deposited coordinate data.\n This is the total count of monomers with reported coordinate data for all polymer\n entity instances in the deposited coordinate data.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deposited_nonpolymer_entity_instance_count": {
            "type": "integer",
            "description": "The number of non-polymer instances in the deposited data set.\n This is the total count of non-polymer entity instances reported\n per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deposited_polymer_entity_instance_count": {
            "type": "integer",
            "description": "The number of polymer instances in the deposited data set.\n This is the total count of polymer entity instances reported\n per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deposited_polymer_monomer_count": {
            "type": "integer",
            "description": "The number of polymer monomers in sample entity instances in the deposited data set.\n This is the total count of monomers for all polymer entity instances reported\n per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deposited_solvent_atom_count": {
            "type": "integer",
            "description": "The number of heavy solvent atom coordinates records per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "deposited_unmodeled_polymer_monomer_count": {
            "type": "integer",
            "description": "The number of unmodeled polymer monomers in the deposited coordinate data. This is\n the total count of monomers with unreported coordinate data for all polymer\n entity instances per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "diffrn_radiation_wavelength_maximum": {
            "type": "number",
            "description": "The maximum radiation wavelength in angstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "diffrn_radiation_wavelength_minimum": {
            "type": "number",
            "description": "The minimum radiation wavelength in angstroms.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "disulfide_bond_count": {
            "type": "integer",
            "description": "The number of disulfide bonds per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "entity_count": {
            "type": "integer",
            "description": "The number of distinct polymer, non-polymer, branched molecular, and solvent entities per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "experimental_method": {
            "type": "string",
            "description": "The category of experimental method(s) used to determine the structure entry.",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        },
        "experimental_method_count": {
            "type": "integer",
            "description": "The number of experimental methods contributing data to the structure determination.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "ihm_multi_scale_flag": {
            "type": "string",
            "description": "Multi-scale modeling flag for integrative structures.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "ihm_multi_state_flag": {
            "type": "string",
            "description": "Multi-state modeling flag for integrative structures.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "ihm_ordered_state_flag": {
            "type": "string",
            "description": "Ordered-state modeling flag for integrative structures.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "ihm_structure_description": {
            "type": "string",
            "description": "Description of the integrative structure.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "inter_mol_covalent_bond_count": {
            "type": "integer",
            "description": "The number of intermolecular covalent bonds.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "inter_mol_metalic_bond_count": {
            "type": "integer",
            "description": "The number of intermolecular metalic bonds.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "molecular_weight": {
            "type": "number",
            "description": "The molecular mass (KDa) of polymer and non-polymer entities (exclusive of solvent) in the deposited structure entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "na_polymer_entity_types": {
            "type": "string",
            "description": "Nucleic acid polymer entity type categories describing the entry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "nonpolymer_entity_count": {
            "type": "integer",
            "description": "The number of distinct non-polymer entities in the structure entry exclusive of solvent.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "nonpolymer_molecular_weight_maximum": {
            "type": "number",
            "description": "The maximum molecular mass (KDa) of a non-polymer entity in the deposited structure entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "nonpolymer_molecular_weight_minimum": {
            "type": "number",
            "description": "The minimum molecular mass (KDa) of a non-polymer entity in the deposited structure entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_composition": {
            "type": "string",
            "description": "Categories describing the polymer entity composition for the entry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count": {
            "type": "integer",
            "description": "The number of distinct polymer entities in the structure entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count_DNA": {
            "type": "integer",
            "description": "The number of distinct DNA polymer entities.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count_RNA": {
            "type": "integer",
            "description": "The number of distinct RNA polymer entities.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count_nucleic_acid": {
            "type": "integer",
            "description": "The number of distinct nucleic acid polymer entities (DNA or RNA).",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count_nucleic_acid_hybrid": {
            "type": "integer",
            "description": "The number of distinct hybrid nucleic acid polymer entities.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_count_protein": {
            "type": "integer",
            "description": "The number of distinct protein polymer entities.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_entity_taxonomy_count": {
            "type": "integer",
            "description": "The number of distinct taxonomies represented among the polymer entities in the entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_molecular_weight_maximum": {
            "type": "number",
            "description": "The maximum molecular mass (KDa) of a polymer entity in the deposited structure entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_molecular_weight_minimum": {
            "type": "number",
            "description": "The minimum molecular mass (KDa) of a polymer entity in the deposited structure entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_monomer_count_maximum": {
            "type": "integer",
            "description": "The maximum monomer count of a polymer entity per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "polymer_monomer_count_minimum": {
            "type": "integer",
            "description": "The minimum monomer count of a polymer entity per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "resolution_combined": {
            "type": "number",
            "description": "Combined estimates of experimental resolution contributing to the refined structural model.\n Resolution reported in \"refine.ls_d_res_high\" is used for X-RAY DIFFRACTION, FIBER DIFFRACTION, \n POWDER DIFFRACTION, ELECTRON CRYSTALLOGRAPHY, and NEUTRON DIFFRACTION as identified in\n \"refine.pdbx_refine_id\". \n Resolution reported in \"em_3d_reconstruction.resolution\" is used for ELECTRON MICROSCOPY. \n The best value corresponding to \"em_3d_reconstruction.resolution_method\" == \"FSC 0.143 CUT-OFF\" \n is used, if available. If not, the best \"em_3d_reconstruction.resolution\" value is used. \n For structures that are not obtained from diffraction-based methods, the resolution values in \n \"refine.ls_d_res_high\" are ignored.\n Multiple values are reported only if multiple methods are used in the structure determination.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "selected_polymer_entity_types": {
            "type": "string",
            "description": "Selected polymer entity type categories describing the entry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "software_programs_combined": {
            "type": "string",
            "description": "Combined list of software programs names reported in connection with the production of this entry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "solvent_entity_count": {
            "type": "integer",
            "description": "The number of distinct solvent entities per deposited structure model.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "structure_determination_methodology": {
            "type": "string",
            "description": "Indicates if the structure was determined using experimental or computational methods.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "structure_determination_methodology_priority": {
            "type": "integer",
            "description": "Indicates the priority of the value in _rcsb_entry_info.structure_determination_methodology.\n The lower the number the higher the priority.\n Priority values for \"experimental\" structures is currently set to 10 and\n the values for \"computational\" structures is set to 100.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "diffrn_resolution_high": {
            "value": {
                "type": "number",
                "description": "The high resolution limit of data collection.",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_external_references": {
        "type": {
            "type": "string",
            "description": "Internal identifier for external resources",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_ihm_dataset_list": {
        "name": {
            "type": "string",
            "description": "Name of input dataset used in integrative modeling.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_ihm_dataset_source_db_reference": {
        "accession_code": {
            "type": "string",
            "description": "Accession code for the input dataset.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "db_name": {
            "type": "string",
            "description": "Name of the source database for the input dataset.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_ma_qa_metric_global": {
        "ma_qa_metric_global": {
            "type": {
                "type": "string",
                "description": "The type of global QA metric.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "value": {
                "type": "number",
                "description": "Value of the global QA metric.",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_primary_citation": {
        "book_title": {
            "type": "string",
            "description": "The title of the book in which the citation appeared; relevant\n for books or book chapters.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "id": {
            "type": "string",
            "description": "The value of _rcsb_primary_citation.id must uniquely identify a record in the\n CITATION list.\n\n The _rcsb_primary_citation.id 'primary' should be used to indicate the\n citation that the author(s) consider to be the most pertinent to\n the contents of the data block.\n\n Note that this item need not be a number; it can be any unique\n identifier.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "journal_abbrev": {
            "type": "string",
            "description": "Abbreviated name of the cited journal as given in the\n Chemical Abstracts Service Source Index.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "journal_id_ASTM": {
            "type": "string",
            "description": "The American Society for Testing and Materials (ASTM) code\n assigned to the journal cited (also referred to as the CODEN\n designator of the Chemical Abstracts Service); relevant for\n journal articles.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "journal_id_ISSN": {
            "type": "string",
            "description": "The International Standard Serial Number (ISSN) code assigned to\n the journal cited; relevant for journal articles.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "pdbx_database_id_DOI": {
            "type": "string",
            "description": "Document Object Identifier used by doi.org to uniquely\n specify bibliographic entry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_ORCID_identifiers": {
            "type": "string",
            "description": "The Open Researcher and Contributor ID (ORCID) identifiers for the citation authors.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_authors": {
            "type": "string",
            "description": "Names of the authors of the citation; relevant for journal\n articles, books and book chapters.  Names are separated by vertical bars.\n\n The family name(s), followed by a comma and including any\n dynastic components, precedes the first name(s) or initial(s).",
            "search": [
                "exact-match",
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        },
        "rcsb_journal_abbrev": {
            "type": "string",
            "description": "Normalized journal abbreviation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "title": {
            "type": "string",
            "description": "The title of the citation; relevant for journal articles, books\n and book chapters.",
            "search": [
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        },
        "year": {
            "type": "integer",
            "description": "The year of the citation; relevant for journal articles, books\n and book chapters.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "refine": {
        "B_iso_mean": {
            "type": "number",
            "description": "The mean isotropic displacement parameter (B value)\n for the coordinate set.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "details": {
            "type": "string",
            "description": "Description of special aspects of the refinement process.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "ls_R_factor_R_free": {
            "type": "number",
            "description": "Residual factor R for reflections that satisfy the resolution\n limits established by _refine.ls_d_res_high and\n _refine.ls_d_res_low and the observation limit established by\n _reflns.observed_criterion, and that were used as the test\n reflections (i.e. were excluded from the refinement) when the\n refinement included the calculation of a 'free' R factor.\n Details of how reflections were assigned to the working and\n test sets are given in _reflns.R_free_details.\n\n     sum|F~obs~ - F~calc~|\n R = ---------------------\n          sum|F~obs~|\n\n F~obs~  = the observed structure-factor amplitudes\n F~calc~ = the calculated structure-factor amplitudes\n\n sum is taken over the specified reflections",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "ls_R_factor_R_work": {
            "type": "number",
            "description": "Residual factor R for reflections that satisfy the resolution\n limits established by _refine.ls_d_res_high and\n _refine.ls_d_res_low and the observation limit established by\n _reflns.observed_criterion, and that were used as the working\n reflections (i.e. were included in the refinement)  when the\n refinement included the calculation of a 'free' R factor.\n Details of how reflections were assigned to the working and\n test sets are given in _reflns.R_free_details.\n\n _refine.ls_R_factor_obs should not be confused with\n _refine.ls_R_factor_R_work; the former reports the results of a\n refinement in which all observed reflections were used, the\n latter a refinement in which a subset of the observed\n reflections were excluded from refinement for the calculation\n of a 'free' R factor. However, it would be meaningful to quote\n both values if a 'free' R factor were calculated for most of\n the refinement, but all of the observed reflections were used\n in the final rounds of refinement; such a protocol should be\n explained in _refine.details.\n\n     sum|F~obs~ - F~calc~|\n R = ---------------------\n          sum|F~obs~|\n\n F~obs~  = the observed structure-factor amplitudes\n F~calc~ = the calculated structure-factor amplitudes\n\n sum is taken over the specified reflections",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "ls_R_factor_all": {
            "type": "number",
            "description": "Residual factor R for all reflections that satisfy the resolution\n limits established by _refine.ls_d_res_high and\n _refine.ls_d_res_low.\n\n     sum|F~obs~ - F~calc~|\n R = ---------------------\n          sum|F~obs~|\n\n F~obs~  = the observed structure-factor amplitudes\n F~calc~ = the calculated structure-factor amplitudes\n\n sum is taken over the specified reflections",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "ls_R_factor_obs": {
            "type": "number",
            "description": "Residual factor R for reflections that satisfy the resolution\n limits established by _refine.ls_d_res_high and\n _refine.ls_d_res_low and the observation limit established by\n _reflns.observed_criterion.\n\n _refine.ls_R_factor_obs should not be confused with\n _refine.ls_R_factor_R_work; the former reports the results of a\n refinement in which all observed reflections were used, the\n latter a refinement in which a subset of the observed\n reflections were excluded from refinement for the calculation\n of a 'free' R factor. However, it would be meaningful to quote\n both values if a 'free' R factor were calculated for most of\n the refinement, but all of the observed reflections were used\n in the final rounds of refinement; such a protocol should be\n explained in _refine.details.\n\n     sum|F~obs~ - F~calc~|\n R = ---------------------\n          sum|F~obs~|\n\n F~obs~  = the observed structure-factor amplitudes\n F~calc~ = the calculated structure-factor amplitudes\n\n sum is taken over the specified reflections",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "pdbx_method_to_determine_struct": {
            "type": "string",
            "description": "Method(s) used to determine the structure.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "reflns": {
        "B_iso_Wilson_estimate": {
            "type": "number",
            "description": "The value of the overall isotropic displacement parameter\n estimated from the slope of the Wilson plot.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "R_free_details": {
            "type": "string",
            "description": "A description of the method by which a subset of reflections was\n selected for exclusion from refinement so as to be used in the\n calculation of a 'free' R factor.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "d_resolution_high": {
            "type": "number",
            "description": "The smallest value in angstroms for the interplanar spacings\n for the reflection data. This is called the highest resolution.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "data_reduction_details": {
            "type": "string",
            "description": "A description of special aspects of the data-reduction\n procedures.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "data_reduction_method": {
            "type": "string",
            "description": "The method used for data reduction.\n\n Note that this is not the computer program used, which is\n described in the SOFTWARE category, but the method\n itself.\n\n This data item should be used to describe significant\n methodological options used within the data-reduction programs.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_Rmerge_I_obs": {
            "type": "number",
            "description": "The R value for merging intensities satisfying the observed\n criteria in this data set.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "pdbx_redundancy": {
            "type": "number",
            "description": "Overall redundancy for this data set.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "percent_possible_obs": {
            "type": "number",
            "description": "The percentage of geometrically possible reflections represented\n by reflections that satisfy the resolution limits established\n by _reflns.d_resolution_high and _reflns.d_resolution_low and\n the observation limit established by\n _reflns.observed_criterion.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "software": {
        "classification": {
            "type": "string",
            "description": "The classification of the program according to its\n major function.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "language": {
            "type": "string",
            "description": "The major computing language in which the software is\n coded.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "The name of the software.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "The classification of the software according to the most\n common types.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "struct": {
        "pdbx_CASP_flag": {
            "type": "string",
            "description": "The item indicates whether the entry is a CASP target, a CASD-NMR target,\n or similar target participating in methods development experiments.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "pdbx_model_details": {
            "type": "string",
            "description": "Text description of the methodology which produced this\n model structure.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_model_type_details": {
            "type": "string",
            "description": "A description of the type of structure model.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "title": {
            "type": "string",
            "description": "A title for the data block. The author should attempt to convey\n the essence of the structure archived in the CIF in the title,\n and to distinguish this structural result from others.",
            "search": [
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        }
    },
    "struct_keywords": {
        "pdbx_keywords": {
            "type": "string",
            "description": "Terms characterizing the macromolecular structure.",
            "search": [
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        },
        "text": {
            "type": "string",
            "description": "Keywords describing this structure.",
            "search": [
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        }
    },
    "symmetry": {
        "cell_setting": {
            "type": "string",
            "description": "The cell settings for this space-group symmetry.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "pdbx_full_space_group_name_H_M": {
            "type": "string",
            "description": "Used for PDB space group:\n\n Example: 'C 1 2 1'  (instead of C 2)\n          'P 1 2 1'  (instead of P 2)\n          'P 1 21 1' (instead of P 21)\n          'P 1 1 21' (instead of P 21 -unique C axis)\n          'H 3'      (instead of R 3   -hexagonal)\n          'H 3 2'    (instead of R 3 2 -hexagonal)",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "space_group_name_H_M": {
            "type": "string",
            "description": "Hermann-Mauguin space-group symbol. Note that the\n Hermann-Mauguin symbol does not necessarily contain complete\n information about the symmetry and the space-group origin. If\n used, always supply the FULL symbol from International Tables\n for Crystallography Vol. A (2002) and indicate the origin and\n the setting if it is not implicit. If there is any doubt that\n the equivalent positions can be uniquely deduced from this\n symbol, specify the  _symmetry_equiv.pos_as_xyz or\n _symmetry.space_group_name_Hall  data items as well. Leave\n spaces between symbols referring to\n different axes.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "space_group_name_Hall": {
            "type": "string",
            "description": "Space-group symbol as described by Hall (1981). This symbol\n gives the space-group setting explicitly. Leave spaces between\n the separate components of the symbol.\n\n Ref: Hall, S. R. (1981). Acta Cryst. A37, 517-525; erratum\n (1981) A37, 921.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_pubmed_container_identifiers": {
        "pubmed_id": {
            "type": "integer",
            "description": "UID assigned to each PubMed record.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_pubmed_abstract_text": {
        "type": "string",
        "description": "A concise, accurate and factual mini-version of the paper contents.",
        "search": [
            "full-text"
        ],
        "is_terminal": True
    },
    "rcsb_pubmed_mesh_descriptors_lineage": {
        "id": {
            "type": "string",
            "description": "Identifier for MeSH classification term.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "MeSH classification term.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "depth": {
            "type": "integer",
            "description": "Hierarchy depth.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "entity_poly": {
        "rcsb_entity_polymer_type": {
            "type": "string",
            "description": "A coarse-grained polymer entity type.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_mutation_count": {
            "type": "integer",
            "description": "Number of engineered mutations engineered in the sample sequence.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "rcsb_sample_sequence_length": {
            "type": "integer",
            "description": "The monomer length of the sample sequence.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "entity_src_gen": {
        "gene_src_tissue": {
            "type": "string",
            "description": "The tissue of the natural organism from which the gene was\n obtained.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_description": {
            "type": "string",
            "description": "Information on the source which is not given elsewhere.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_gene_src_atcc": {
            "type": "string",
            "description": "American Type Culture Collection tissue culture number.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_gene_src_cell": {
            "type": "string",
            "description": "Cell type.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_gene_src_cell_line": {
            "type": "string",
            "description": "The specific line of cells.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_gene_src_cellular_location": {
            "type": "string",
            "description": "Identifies the location inside (or outside) the cell.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_gene_src_organ": {
            "type": "string",
            "description": "Organized group of tissues that carries on a specialized function.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_gene_src_organelle": {
            "type": "string",
            "description": "Organized structure within cell.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_atcc": {
            "type": "string",
            "description": "Americal Tissue Culture Collection of the expression system. Where\n full details of the protein production are available it would\n be expected that this item  would be derived from\n _entity_src_gen_express.host_org_culture_collection",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_cell": {
            "type": "string",
            "description": "Cell type from which the gene is derived. Where\n entity.target_id is provided this should be derived from\n details of the target.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_cell_line": {
            "type": "string",
            "description": "A specific line of cells used as the expression system. Where\n full details of the protein production are available it would\n be expected that this item would be derived from\n entity_src_gen_express.host_org_cell_line",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_cellular_location": {
            "type": "string",
            "description": "Identifies the location inside (or outside) the cell which\n expressed the molecule.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_culture_collection": {
            "type": "string",
            "description": "Culture collection of the expression system. Where\n full details of the protein production are available it would\n be expected that this item  would be derived somehwere, but\n exactly where is not clear.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_organ": {
            "type": "string",
            "description": "Specific organ which expressed the molecule.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_organelle": {
            "type": "string",
            "description": "Specific organelle which expressed the molecule.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_tissue": {
            "type": "string",
            "description": "The specific tissue which expressed the molecule. Where full details\n of the protein production are available it would be expected that this\n item would be derived from _entity_src_gen_express.host_org_tissue",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_tissue_fraction": {
            "type": "string",
            "description": "The fraction of the tissue which expressed the\nmolecule.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_vector": {
            "type": "string",
            "description": "Identifies the vector used. Where full details of the protein\n production are available it would be expected that this item\n would be derived from _entity_src_gen_clone.vector_name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_host_org_vector_type": {
            "type": "string",
            "description": "Identifies the type of vector used (plasmid, virus, or cosmid).\n Where full details of the protein production are available it\n would be expected that this item would be derived from\n _entity_src_gen_express.vector_type.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "plasmid_name": {
            "type": "string",
            "description": "The name of the plasmid that produced the entity in the host\n organism. Where full details of the protein production are available\n it would be expected that this item would be derived from\n _pdbx_construct.name of the construct pointed to from\n _entity_src_gen_express.plasmid_id.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "entity_src_nat": {
        "details": {
            "type": "string",
            "description": "A description of special aspects of the organism from which the\n entity was isolated.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_atcc": {
            "type": "string",
            "description": "Americal Tissue Culture Collection number.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_cell": {
            "type": "string",
            "description": "A particular cell type.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_cell_line": {
            "type": "string",
            "description": "The specific line of cells.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_cellular_location": {
            "type": "string",
            "description": "Identifies the location inside (or outside) the cell.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_organ": {
            "type": "string",
            "description": "Organized group of tissues that carries on a specialized function.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_organelle": {
            "type": "string",
            "description": "Organized structure within cell.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_plasmid_details": {
            "type": "string",
            "description": "Details about the plasmid.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pdbx_plasmid_name": {
            "type": "string",
            "description": "The plasmid containing the gene.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "tissue": {
            "type": "string",
            "description": "The tissue of the organism from which the entity was isolated.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "tissue_fraction": {
            "type": "string",
            "description": "The subcellular fraction of the tissue of the organism from\n which the entity was isolated.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_cluster_membership": {
        "cluster_id": {
            "type": "integer",
            "description": "Identifier for a cluster at the specified level of sequence identity within the cluster data set.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "identity": {
            "type": "integer",
            "description": "Sequence identity expressed as an integer percent value.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_entity_host_organism": {
        "common_name": {
            "type": "string",
            "description": "The common name of the host organism",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "ncbi_common_names": {
            "type": "string",
            "description": "Common names associated with this taxonomy code obtained from NCBI Taxonomy Database.\n\n  These names correspond to the taxonomy identifier assigned by the PDB depositor.\n\nReferences:\n\nSayers EW, Barrett T, Benson DA, Bryant SH, Canese K, Chetvernin V,\nChurch DM, DiCuccio M, Edgar R, Federhen S, Feolo M, Geer LY,\nHelmberg W, Kapustin Y, Landsman D, Lipman DJ, Madden TL, Maglott DR,\nMiller V, Mizrachi I, Ostell J, Pruitt KD, Schuler GD, Sequeira E,\nSherry ST, Shumway M, Sirotkin K, Souvorov A, Starchenko G,\nTatusova TA, Wagner L, Yaschenko E, Ye J (2009). Database resources\nof the National Center for Biotechnology Information. Nucleic Acids\nRes. 2009 Jan;37(Database issue):D5-15. Epub 2008 Oct 21.\n\nBenson DA, Karsch-Mizrachi I, Lipman DJ, Ostell J, Sayers EW (2009).\nGenBank. Nucleic Acids Res. 2009 Jan;37(Database issue):D26-31.\nEpub 2008 Oct 21.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "ncbi_parent_scientific_name": {
            "type": "string",
            "description": "The parent scientific name in the NCBI taxonomy hierarchy (depth=1) associated with this taxonomy code.\n\nReferences:\n\nSayers EW, Barrett T, Benson DA, Bryant SH, Canese K, Chetvernin V,\nChurch DM, DiCuccio M, Edgar R, Federhen S, Feolo M, Geer LY,\nHelmberg W, Kapustin Y, Landsman D, Lipman DJ, Madden TL, Maglott DR,\nMiller V, Mizrachi I, Ostell J, Pruitt KD, Schuler GD, Sequeira E,\nSherry ST, Shumway M, Sirotkin K, Souvorov A, Starchenko G,\nTatusova TA, Wagner L, Yaschenko E, Ye J (2009). Database resources\nof the National Center for Biotechnology Information. Nucleic Acids\nRes. 2009 Jan;37(Database issue):D5-15. Epub 2008 Oct 21.\n\nBenson DA, Karsch-Mizrachi I, Lipman DJ, Ostell J, Sayers EW (2009).\nGenBank. Nucleic Acids Res. 2009 Jan;37(Database issue):D26-31.\nEpub 2008 Oct 21.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "ncbi_scientific_name": {
            "type": "string",
            "description": "The scientific name associated with this taxonomy code aggregated by the NCBI Taxonomy Database.\n\n  This name corresponds to the taxonomy identifier assigned by the PDB depositor.\n\n\nReferences:\n\nSayers EW, Barrett T, Benson DA, Bryant SH, Canese K, Chetvernin V,\nChurch DM, DiCuccio M, Edgar R, Federhen S, Feolo M, Geer LY,\nHelmberg W, Kapustin Y, Landsman D, Lipman DJ, Madden TL, Maglott DR,\nMiller V, Mizrachi I, Ostell J, Pruitt KD, Schuler GD, Sequeira E,\nSherry ST, Shumway M, Sirotkin K, Souvorov A, Starchenko G,\nTatusova TA, Wagner L, Yaschenko E, Ye J (2009). Database resources\nof the National Center for Biotechnology Information. Nucleic Acids\nRes. 2009 Jan;37(Database issue):D5-15. Epub 2008 Oct 21.\n\nBenson DA, Karsch-Mizrachi I, Lipman DJ, Ostell J, Sayers EW (2009).\nGenBank. Nucleic Acids Res. 2009 Jan;37(Database issue):D26-31.\nEpub 2008 Oct 21.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "scientific_name": {
            "type": "string",
            "description": "The scientific name of the host organism",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "taxonomy_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the NCBI Taxonomy lineage as parent taxonomy lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the NCBI Taxonomy lineage as parent taxonomy idcodes.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the NCBI Taxonomy lineage as parent taxonomy names.",
                "search": [
                    "exact-match",
                    "full-text",
                    "suggest"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_entity_source_organism": {
        "common_name": {
            "type": "string",
            "description": "The common name for the source organism assigned by the PDB depositor.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "ncbi_common_names": {
            "type": "string",
            "description": "Common names associated with this taxonomy code aggregated by the NCBI Taxonomy Database.\n\n  These name correspond to the taxonomy identifier assigned by the PDB depositor.\n\nReferences:\n\nSayers EW, Barrett T, Benson DA, Bryant SH, Canese K, Chetvernin V,\nChurch DM, DiCuccio M, Edgar R, Federhen S, Feolo M, Geer LY,\nHelmberg W, Kapustin Y, Landsman D, Lipman DJ, Madden TL, Maglott DR,\nMiller V, Mizrachi I, Ostell J, Pruitt KD, Schuler GD, Sequeira E,\nSherry ST, Shumway M, Sirotkin K, Souvorov A, Starchenko G,\nTatusova TA, Wagner L, Yaschenko E, Ye J (2009). Database resources\nof the National Center for Biotechnology Information. Nucleic Acids\nRes. 2009 Jan;37(Database issue):D5-15. Epub 2008 Oct 21.\n\nBenson DA, Karsch-Mizrachi I, Lipman DJ, Ostell J, Sayers EW (2009).\nGenBank. Nucleic Acids Res. 2009 Jan;37(Database issue):D26-31.\nEpub 2008 Oct 21.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "ncbi_parent_scientific_name": {
            "type": "string",
            "description": "A parent scientific name in the NCBI taxonomy hierarchy of the source organism assigned by the PDB depositor.\n  For cellular organism this corresponds to a superkingdom (e.g., Archaea, Bacteria, Eukaryota).  For viruses this\n  corresponds to a clade (e.g.  Adnaviria, Bicaudaviridae, Clavaviridae). For other and unclassified entries this\n  corresponds to the first level of any taxonomic rank below the root level.\n\nReferences:\n\nSayers EW, Barrett T, Benson DA, Bryant SH, Canese K, Chetvernin V,\nChurch DM, DiCuccio M, Edgar R, Federhen S, Feolo M, Geer LY,\nHelmberg W, Kapustin Y, Landsman D, Lipman DJ, Madden TL, Maglott DR,\nMiller V, Mizrachi I, Ostell J, Pruitt KD, Schuler GD, Sequeira E,\nSherry ST, Shumway M, Sirotkin K, Souvorov A, Starchenko G,\nTatusova TA, Wagner L, Yaschenko E, Ye J (2009). Database resources\nof the National Center for Biotechnology Information. Nucleic Acids\nRes. 2009 Jan;37(Database issue):D5-15. Epub 2008 Oct 21.\n\nBenson DA, Karsch-Mizrachi I, Lipman DJ, Ostell J, Sayers EW (2009).\nGenBank. Nucleic Acids Res. 2009 Jan;37(Database issue):D26-31.\nEpub 2008 Oct 21.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "ncbi_scientific_name": {
            "type": "string",
            "description": "The scientific name associated with this taxonomy code aggregated by the NCBI Taxonomy Database.\n\n  This name corresponds to the taxonomy identifier assigned by the PDB depositor.\n\n\nReferences:\n\nSayers EW, Barrett T, Benson DA, Bryant SH, Canese K, Chetvernin V,\nChurch DM, DiCuccio M, Edgar R, Federhen S, Feolo M, Geer LY,\nHelmberg W, Kapustin Y, Landsman D, Lipman DJ, Madden TL, Maglott DR,\nMiller V, Mizrachi I, Ostell J, Pruitt KD, Schuler GD, Sequeira E,\nSherry ST, Shumway M, Sirotkin K, Souvorov A, Starchenko G,\nTatusova TA, Wagner L, Yaschenko E, Ye J (2009). Database resources\nof the National Center for Biotechnology Information. Nucleic Acids\nRes. 2009 Jan;37(Database issue):D5-15. Epub 2008 Oct 21.\n\nBenson DA, Karsch-Mizrachi I, Lipman DJ, Ostell J, Sayers EW (2009).\nGenBank. Nucleic Acids Res. 2009 Jan;37(Database issue):D26-31.\nEpub 2008 Oct 21.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "scientific_name": {
            "type": "string",
            "description": "The scientific name of the source organism assigned by the PDB depositor.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "source_type": {
            "type": "string",
            "description": "The source type for the entity",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "taxonomy_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the NCBI Taxonomy lineage as parent taxonomy lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the NCBI Taxonomy lineage as parent taxonomy idcodes.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Memebers of the NCBI Taxonomy lineage as parent taxonomy names.",
                "search": [
                    "exact-match",
                    "full-text",
                    "suggest"
                ],
                "is_terminal": True
            }
        },
        "rcsb_gene_name": {
            "value": {
                "type": "string",
                "description": "Gene name.",
                "search": [
                    "exact-match",
                    "suggest"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_genomic_lineage": {
        "id": {
            "type": "string",
            "description": "Automatically assigned ID that uniquely identifies taxonomy, chromosome or gene in the Genome Location Browser.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_membrane_lineage": {
        "depth": {
            "type": "integer",
            "description": "Hierarchy depth.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "id": {
            "type": "string",
            "description": "Automatically assigned ID for membrane classification term in the Membrane Protein Browser.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "Membrane protein classification term.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_polymer_entity": {
        "formula_weight": {
            "type": "number",
            "description": "Formula mass (KDa) of the entity.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "pdbx_description": {
            "type": "string",
            "description": "A description of the polymer entity.",
            "search": [
                "exact-match",
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        },
        "pdbx_number_of_molecules": {
            "type": "integer",
            "description": "The number of molecules of the entity in the entry.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "rcsb_source_part_count": {
            "type": "integer",
            "description": "The number of biological sources for the polymer entity. Multiple source contributions\n may come from the same organism (taxonomy).",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "rcsb_source_taxonomy_count": {
            "type": "integer",
            "description": "The number of distinct source taxonomies for the polymer entity. Commonly used to identify chimeric polymers.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "rcsb_ec_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the enzyme classification lineage as parent classification hierarchy depth (1-N).",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the enzyme classification lineage as parent classification codes.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the enzyme classification lineage as parent classification names.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            }
        },
        "rcsb_macromolecular_names_combined": {
            "name": {
                "type": "string",
                "description": "Combined list of macromolecular names.",
                "search": [
                    "full-text"
                ],
                "is_terminal": True
            }
        },
        "rcsb_enzyme_class_combined": {
            "depth": {
                "type": "integer",
                "description": "The enzyme classification hierarchy depth (1-N).",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "ec": {
                "type": "string",
                "description": "Combined list of enzyme class assignments.",
                "search": [
                    "exact-match",
                    "full-text"
                ],
                "is_terminal": True
            },
            "provenance_source": {
                "type": "string",
                "description": "Combined list of enzyme class associated provenance sources.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            }
        },
        "rcsb_polymer_name_combined": {
            "names": {
                "type": "string",
                "description": "Protein name annotated by the UniProtKB or macromolecular name assigned by the PDB.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_polymer_entity_annotation": {
        "annotation_id": {
            "type": "string",
            "description": "An identifier for the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "A description for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "A type or category of the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "annotation_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the annotation lineage as parent lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class identifiers.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class names.",
                "search": [
                    "exact-match",
                    "full-text"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_polymer_entity_container_identifiers": {
        "chem_comp_monomers": {
            "type": "string",
            "description": "Unique list of monomer chemical component identifiers in the polymer entity in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "chem_ref_def_id": {
            "type": "string",
            "description": "The chemical reference definition identifier for the entity in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "entry_id": {
            "type": "string",
            "description": "Entry identifier for the container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "prd_id": {
            "type": "string",
            "description": "The BIRD identifier for the entity in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_id": {
            "type": "string",
            "description": "A unique identifier for each object in this entity container formed by\n an underscore separated concatenation of entry and entity identifiers.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "reference_sequence_identifiers": {
            "database_accession": {
                "type": "string",
                "description": "Reference database accession code",
                "search": [
                    "exact-match",
                    "suggest"
                ],
                "is_terminal": True
            },
            "database_isoform": {
                "type": "string",
                "description": "Reference database identifier for the sequence isoform",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "database_name": {
                "type": "string",
                "description": "Reference database name",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "entity_sequence_coverage": {
                "type": "number",
                "description": "Indicates what fraction of this polymer entity sequence is covered by the reference sequence.",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "reference_sequence_coverage": {
                "type": "number",
                "description": "Indicates what fraction of the reference sequence is covered by this polymer entity sequence.",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_polymer_entity_feature_summary": {
        "count": {
            "type": "integer",
            "description": "The feature count.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "coverage": {
            "type": "number",
            "description": "The fractional feature coverage relative to the full entity sequence.\n For instance, the fraction of features such as mutations, artifacts or modified monomers\n relative to the length of the entity sequence.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "maximum_length": {
            "type": "integer",
            "description": "The maximum feature length.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "minimum_length": {
            "type": "integer",
            "description": "The minimum feature length.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "Type or category of the feature.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_polymer_entity_group_membership": {
        "aggregation_method": {
            "type": "string",
            "description": "Method used to establish group membership",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "group_id": {
            "type": "string",
            "description": "A unique identifier for a group of entities",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "similarity_cutoff": {
            "type": "number",
            "description": "Degree of similarity expressed as a floating-point number",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_polymer_entity_keywords": {
        "text": {
            "type": "string",
            "description": "Keywords describing this polymer entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_polymer_entity_name_com": {
        "name": {
            "type": "string",
            "description": "A common name for the polymer entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_polymer_entity_name_sys": {
        "name": {
            "type": "string",
            "description": "The systematic name for the polymer entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "drugbank_container_identifiers": {
        "drugbank_id": {
            "type": "string",
            "description": "The DrugBank accession code",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "drugbank_info": {
        "affected_organisms": {
            "type": "string",
            "description": "The DrugBank drug affected organisms.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "atc_codes": {
            "type": "string",
            "description": "The Anatomical Therapeutic Chemical Classification System (ATC) codes.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "brand_names": {
            "type": "string",
            "description": "DrugBank drug brand names.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "cas_number": {
            "type": "string",
            "description": "The DrugBank assigned Chemical Abstracts Service identifier.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "The DrugBank drug description.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "drug_categories": {
            "type": "string",
            "description": "The DrugBank drug categories.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "drug_groups": {
            "type": "string",
            "description": "The DrugBank drug groups determine their drug development status.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "indication": {
            "type": "string",
            "description": "The DrugBank drug indication.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "mechanism_of_action": {
            "type": "string",
            "description": "The DrugBank drug mechanism of actions.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "The DrugBank drug name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pharmacology": {
            "type": "string",
            "description": "The DrugBank drug pharmacology.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "synonyms": {
            "type": "string",
            "description": "DrugBank drug name synonyms.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "drug_products": {
            "approved": {
                "type": "string",
                "description": "Indicates whether this drug has been approved by the regulating government.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "country": {
                "type": "string",
                "description": "The country where this commercially available drug has been approved.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "ended_marketing_on": {
                "type": "string",
                "description": "The ending date for market approval.",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "started_marketing_on": {
                "type": "string",
                "description": "The starting date for market approval.",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            }
        }
    },
    "drugbank_target": {
        "interaction_type": {
            "type": "string",
            "description": "The type of target interaction.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "The target name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "organism_common_name": {
            "type": "string",
            "description": "The organism common name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "target_actions": {
            "type": "string",
            "description": "The actions of the target interaction.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    }
}

RCSB_CHEMICAL_SCHEMA = {
    "chem_comp": {
        "formula_weight": {
            "type": "number",
            "description": "Formula mass of the chemical component.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "The full name of the component.",
            "search": [
                "exact-match",
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "For standard polymer components, the type of the monomer.\n Note that monomers that will form polymers are of three types:\n linking monomers, monomers with some type of N-terminal (or 5')\n cap and monomers with some type of C-terminal (or 3') cap.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_reference_molecule": {
        "class": {
            "type": "string",
            "description": "Broadly defines the function of the entity.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "Description of this molecule.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name of the entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "prd_id": {
            "type": "string",
            "description": "The value of _pdbx_reference_molecule.prd_id is the unique identifier\n for the reference molecule in this family.\n\n By convention this ID uniquely identifies the reference molecule in\n in the PDB reference dictionary.\n\n The ID has the template form PRD_dddddd (e.g. PRD_000001)",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "Defines the structural classification of the entity.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "pdbx_reference_molecule_family": {
        "name": {
            "type": "string",
            "description": "The entity family name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_reference_molecule_related_structures": {
        "db_code": {
            "type": "string",
            "description": "The database identifier code for the related structure reference.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "pdbx_reference_molecule_synonyms": {
        "name": {
            "type": "string",
            "description": "A synonym name for the entity.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_annotation": {
        "annotation_id": {
            "type": "string",
            "description": "An identifier for the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "A description for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "A name for the annotation.",
            "search": [
                "exact-match",
                "full-text"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "A type or category of the annotation.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "annotation_lineage": {
            "depth": {
                "type": "integer",
                "description": "Members of the annotation lineage as parent lineage depth (1-N)",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "id": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class identifiers.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "name": {
                "type": "string",
                "description": "Members of the annotation lineage as parent class names.",
                "search": [
                    "exact-match",
                    "full-text"
                ],
                "is_terminal": True
            }
        }
    },
    "rcsb_chem_comp_container_identifiers": {
        "comp_id": {
            "type": "string",
            "description": "The chemical component identifier.",
            "search": [
                "exact-match",
                "suggest"
            ],
            "is_terminal": True
        },
        "drugbank_id": {
            "type": "string",
            "description": "The DrugBank identifier corresponding to the chemical component.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "prd_id": {
            "type": "string",
            "description": "The BIRD definition identifier.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "rcsb_id": {
            "type": "string",
            "description": "A unique identifier for the chemical definition in this container.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_descriptor": {
        "InChIKey": {
            "type": "string",
            "description": "Standard IUPAC International Chemical Identifier (InChI) descriptor key\n for the chemical component\n\n InChI, the IUPAC International Chemical Identifier,\n by Stephen R Heller, Alan McNaught, Igor Pletnev, Stephen Stein and Dmitrii Tchekhovskoi,\n Journal of Cheminformatics, 2015, 7:23",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_info": {
        "atom_count_chiral": {
            "type": "integer",
            "description": "Chemical component chiral atom count",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "atom_count_heavy": {
            "type": "integer",
            "description": "Chemical component heavy atom count",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "bond_count": {
            "type": "integer",
            "description": "Chemical component total bond count",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "bond_count_aromatic": {
            "type": "integer",
            "description": "Chemical component aromatic bond count",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "initial_deposition_date": {
            "type": "string",
            "description": "The date the chemical definition was first deposited in the PDB repository.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        },
        "initial_release_date": {
            "type": "string",
            "description": "The initial date the chemical definition was released in the PDB repository.",
            "search": [
                "default-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_related": {
        "resource_accession_code": {
            "type": "string",
            "description": "The resource identifier code for the related chemical reference.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "resource_name": {
            "type": "string",
            "description": "The resource name for the related chemical reference.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_synonyms": {
        "name": {
            "type": "string",
            "description": "The synonym of this particular chemical component.",
            "search": [
                "full-text",
                "suggest"
            ],
            "is_terminal": True
        },
        "provenance_source": {
            "type": "string",
            "description": "The provenance of this synonym.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "type": {
            "type": "string",
            "description": "This data item contains the synonym type.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "rcsb_chem_comp_target": {
        "name": {
            "type": "string",
            "description": "The chemical component target name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    },
    "rcsb_id": {
        "type": "string",
        "description": "A unique identifier for the chemical definition in this container.",
        "search": [
            "exact-match"
        ],
        "is_terminal": True
    },
    "drugbank_container_identifiers": {
        "drugbank_id": {
            "type": "string",
            "description": "The DrugBank accession code",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        }
    },
    "drugbank_info": {
        "affected_organisms": {
            "type": "string",
            "description": "The DrugBank drug affected organisms.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "atc_codes": {
            "type": "string",
            "description": "The Anatomical Therapeutic Chemical Classification System (ATC) codes.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "brand_names": {
            "type": "string",
            "description": "DrugBank drug brand names.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "cas_number": {
            "type": "string",
            "description": "The DrugBank assigned Chemical Abstracts Service identifier.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "description": {
            "type": "string",
            "description": "The DrugBank drug description.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "drug_categories": {
            "type": "string",
            "description": "The DrugBank drug categories.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "drug_groups": {
            "type": "string",
            "description": "The DrugBank drug groups determine their drug development status.",
            "search": [
                "exact-match"
            ],
            "is_terminal": True
        },
        "indication": {
            "type": "string",
            "description": "The DrugBank drug indication.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "mechanism_of_action": {
            "type": "string",
            "description": "The DrugBank drug mechanism of actions.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "The DrugBank drug name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "pharmacology": {
            "type": "string",
            "description": "The DrugBank drug pharmacology.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "synonyms": {
            "type": "string",
            "description": "DrugBank drug name synonyms.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "drug_products": {
            "approved": {
                "type": "string",
                "description": "Indicates whether this drug has been approved by the regulating government.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "country": {
                "type": "string",
                "description": "The country where this commercially available drug has been approved.",
                "search": [
                    "exact-match"
                ],
                "is_terminal": True
            },
            "ended_marketing_on": {
                "type": "string",
                "description": "The ending date for market approval.",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            },
            "started_marketing_on": {
                "type": "string",
                "description": "The starting date for market approval.",
                "search": [
                    "default-match"
                ],
                "is_terminal": True
            }
        }
    },
    "drugbank_target": {
        "interaction_type": {
            "type": "string",
            "description": "The type of target interaction.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "name": {
            "type": "string",
            "description": "The target name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "organism_common_name": {
            "type": "string",
            "description": "The organism common name.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        },
        "target_actions": {
            "type": "string",
            "description": "The actions of the target interaction.",
            "search": [
                "full-text"
            ],
            "is_terminal": True
        }
    }
}

def get_attribute_names(schema, prefix=""):
    """Takes a schema-describing object (such as RCSB_METADATA_SCHEMA or
    RCSB_CHEMICAL_SCHEMA) and returns a list of all attribute names that it
    implies are allowed.

    :param dict schema: The schema-describing object.
    :param str prefix: Prefix prepended to attributes (used in recursive calls).
    :rtype: list[str]"""
    
    names = []
    for k, v in schema.items():
        value = f"{prefix}{'.' if prefix else ''}{k}"
        if v.get("is_terminal"):
            names.append(value)
        else:
            names.extend(get_attribute_names(v, prefix=value))
    return names