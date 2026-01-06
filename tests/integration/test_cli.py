import sys
import json
import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from pdbsearch.__main__ import main

class CliTestCase(TestCase):

    def run_cli(self, *args):
        captured = StringIO()
        with patch.object(sys, "argv", ["pdbsearch"] + list(args)):
            with patch.object(sys, "stdout", captured):
                main()
        return captured.getvalue()



class SchemaFetchTests(CliTestCase):

    def setUp(self):
        self.patch1 = patch("requests.get")
        self.mock_get = self.patch1.start()
        self.mock_get.return_value.json.return_value = {
            "type": "object",
            "properties": {
                "pdbx_entity_nonpoly": {
                    "type": "object",
                    "properties": {
                        "comp_id": {
                            "type": "string",
                            "description": "This data item is a pointer to _chem_comp.id in the CHEM_COMP category.",
                            "rcsb_description": [
                                {
                                    "text": "This data item is a pointer to _chem_comp.id in the CHEM_COMP category.",
                                    "context": "dictionary"
                                }
                            ]
                        },
                        "entity_id": {
                            "type": "string",
                            "description": "This data item is a pointer to _entity.id in the ENTITY category.",
                            "rcsb_description": [
                                {
                                    "text": "This data item is a pointer to _entity.id in the ENTITY category.",
                                    "context": "dictionary"
                                }
                            ]
                        },
                        "name": {
                            "type": "string",
                            "description": "A name for the non-polymer entity",
                            "rcsb_search_context": [
                                "full-text"
                            ],
                            "rcsb_full_text_priority": 1,
                            "rcsb_description": [
                                {
                                    "text": "A name for the non-polymer entity",
                                    "context": "dictionary"
                                },
                                {
                                    "text": "Name (Entity Nonpoly)",
                                    "context": "brief"
                                }
                            ]
                        },
                        "rcsb_prd_id": {
                            "type": "string",
                            "description": "For non-polymer BIRD molecules the BIRD identifier for the entity.",
                            "rcsb_description": [
                                {
                                    "text": "For non-polymer BIRD molecules the BIRD identifier for the entity.",
                                    "context": "dictionary"
                                }
                            ]
                        }
                    },
                    "additionalProperties": False,
                    "required": [
                        "entity_id"
                    ]
                },
                "rcsb_latest_revision": {
                    "type": "object",
                    "properties": {
                        "major_revision": {
                            "type": "integer",
                            "description": "The major version number of the latest revision.",
                            "rcsb_description": [
                                {
                                    "text": "The major version number of the latest revision.",
                                    "context": "dictionary"
                                }
                            ]
                        },
                        "minor_revision": {
                            "type": "integer",
                            "description": "The minor version number of the latest revision.",
                            "rcsb_description": [
                                {
                                    "text": "The minor version number of the latest revision.",
                                    "context": "dictionary"
                                }
                            ]
                        },
                        "revision_date": {
                            "type": "string",
                            "format": "date-time",
                            "examples": [
                                "2020-02-11",
                                "2018-10-23"
                            ],
                            "description": "The release date of the latest revision item.",
                            "rcsb_description": [
                                {
                                    "text": "The release date of the latest revision item.",
                                    "context": "dictionary"
                                }
                            ]
                        }
                    },
                    "additionalProperties": False
                }
            }
        }


    def tearDown(self):
        self.patch1.stop()


    def test_text_schema_fetch(self):
        result = self.run_cli("schema")
        schema = json.loads(result)
        self.assertEqual(schema, {"pdbx_entity_nonpoly.name": ["full-text"]})
        self.mock_get.assert_called_once_with("https://search.rcsb.org/rcsbsearch/v2/metadata/schema", timeout=None)
    

    def test_text_schema_fetch_with_indent(self):
        result = self.run_cli("schema", "--indent", "8")
        schema = json.loads(result)
        self.assertEqual(schema, {"pdbx_entity_nonpoly.name": ["full-text"]})
        self.assertIn("        ", result)
        self.mock_get.assert_called_once_with("https://search.rcsb.org/rcsbsearch/v2/metadata/schema", timeout=None)


    def test_chemical_schema_fetch(self):
        result = self.run_cli("schema", "--chemical")
        schema = json.loads(result)
        self.assertEqual(schema, {"pdbx_entity_nonpoly.name": ["full-text"]})
        self.mock_get.assert_called_once_with("https://search.rcsb.org/rcsbsearch/v2/metadata/chemical/schema", timeout=None)



class ClearSchemaTests(CliTestCase):

    def tearDown(self):
        try:
            os.remove("__test.json")
        except Exception:
            pass


    @patch("pdbsearch.schema.CACHE_FILE", "__test.json")
    def test_clear_schema_when_no_file_exists(self):
        self.run_cli("clearschema")
    

    @patch("pdbsearch.schema.CACHE_FILE", "__test.json")
    def test_clear_schema_when_file_exists(self):
        with open("__test.json", "w") as f: f.write("test")
        self.run_cli("clearschema")
        self.assertFalse(os.path.exists("__test.json"))