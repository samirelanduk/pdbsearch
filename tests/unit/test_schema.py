from unittest import TestCase
from unittest.mock import patch, call
from pdbsearch.schema import fetch_names_from_rcsb_schema, update_terms_from_api
from pdbsearch.schema import process_schema_object, get_attribute_names

class FetchNamesFromRCSBSchemaTests(TestCase):

    @patch("requests.get")
    @patch("pdbsearch.schema.process_schema_object")
    @patch("pdbsearch.schema.get_attribute_names")
    def test_can_fetch_names_from_rcsb_schema(self, mock_get_attribute_names, mock_process_schema_object, mock_get):
        names = fetch_names_from_rcsb_schema()
        self.assertEqual(names, mock_get_attribute_names.return_value)
        mock_get_attribute_names.assert_called_once_with(mock_process_schema_object.return_value)
        mock_process_schema_object.assert_called_once_with(mock_get.return_value.json.return_value)
        mock_get.assert_called_once_with("https://search.rcsb.org/rcsbsearch/v2/metadata/schema", timeout=None)
    

    @patch("requests.get")
    @patch("pdbsearch.schema.process_schema_object")
    @patch("pdbsearch.schema.get_attribute_names")
    def test_can_fetch_names_from_rcsb_schema_with_timeout(self, mock_get_attribute_names, mock_process_schema_object, mock_get):
        names = fetch_names_from_rcsb_schema(timeout=100)
        self.assertEqual(names, mock_get_attribute_names.return_value)
        mock_get_attribute_names.assert_called_once_with(mock_process_schema_object.return_value)
        mock_process_schema_object.assert_called_once_with(mock_get.return_value.json.return_value)
        mock_get.assert_called_once_with("https://search.rcsb.org/rcsbsearch/v2/metadata/schema", timeout=100)
    

    @patch("requests.get")
    @patch("pdbsearch.schema.process_schema_object")
    @patch("pdbsearch.schema.get_attribute_names")
    def test_can_fetch_chemical_names_from_rcsb_schema(self, mock_get_attribute_names, mock_process_schema_object, mock_get):
        names = fetch_names_from_rcsb_schema(chemical=True)
        self.assertEqual(names, mock_get_attribute_names.return_value)
        mock_get_attribute_names.assert_called_once_with(mock_process_schema_object.return_value)
        mock_process_schema_object.assert_called_once_with(mock_get.return_value.json.return_value)
        mock_get.assert_called_once_with("https://search.rcsb.org/rcsbsearch/v2/metadata/chemical/schema", timeout=None)



class UpdateTermsFromAPITests(TestCase):

    def setUp(self):
        from pdbsearch import terms
        self.original_terms = terms.TEXT_TERMS.copy()
        self.original_chem_terms = terms.TEXT_CHEM_TERMS.copy()
    

    def tearDown(self):
        from pdbsearch import terms
        terms.TEXT_TERMS.clear()
        terms.TEXT_TERMS.update(self.original_terms)
        terms.TEXT_CHEM_TERMS.clear()
        terms.TEXT_CHEM_TERMS.update(self.original_chem_terms)
    

    @patch("pdbsearch.schema.fetch_names_from_rcsb_schema")
    def test_can_update_terms(self, mock_fetch_names):
        mock_fetch_names.side_effect = [{1: 2}, {3: 4}]
        self.assertTrue(update_terms_from_api())
        from pdbsearch import terms
        self.assertEqual(terms.TEXT_TERMS, {1: 2})
        self.assertEqual(terms.TEXT_CHEM_TERMS, {3: 4})
        mock_fetch_names.assert_has_calls([
            call(chemical=False, timeout=2),
            call(chemical=True, timeout=2)
        ])
    

    @patch("pdbsearch.schema.fetch_names_from_rcsb_schema")
    def test_can_fail_silently(self, mock_fetch_names):
        mock_fetch_names.side_effect = [{1: 2}, ValueError]
        self.assertFalse(update_terms_from_api())
        from pdbsearch import terms
        self.assertIn("drugbank_target.name", terms.TEXT_TERMS)
        self.assertIn("drugbank_target.name", terms.TEXT_CHEM_TERMS)



class ProcessSchemaObjectTests(TestCase):

    def test_can_process_schema_object(self):
        schema = {
            "type": "object",
            "properties": {
                "key1": {
                    "type": "string",
                    "description": "Description of key1",
                    "rcsb_search_context": ["full-text"]
                },
                "key2": {
                    "type": "string",
                    "description": "Description of key2",
                },
                "key3": {
                    "type": "object",
                    "properties": {
                        "key31": {
                            "type": "number",
                            "description": "Description of key31",
                            "rcsb_search_context": ["default-match"]
                        },
                        "key32": {
                            "type": "string",
                            "description": "Description of key32",
                        },
                        "key33": {
                            "type": "object",
                            "properties": {
                                "key331": {
                                    "anyOf": [{"type": "string"}, {"type": "number"}],
                                    "description": "Description of key331",
                                    "rcsb_search_context": ["full-text"]
                                }
                            }
                        }
                    }
                },
                "key4": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "Description of key4",
                        "rcsb_search_context": ["full-text"]
                    }
                }
            }
        }
        self.assertEqual(process_schema_object(schema), {
            "key1": {
                "type": "string",
                "description": "Description of key1",
                "search": ["full-text"],
                "is_terminal": True
            },
            "key3": {
                "key31": {
                    "type": "number",
                    "description": "Description of key31",
                    "search": ["default-match"],
                    "is_terminal": True
                },
                "key33": {
                    "key331": {
                        "type": ["string", "number"],
                        "description": "Description of key331",
                        "search": ["full-text"],
                        "is_terminal": True
                    }
                }
            },
            "key4": {
                "type": "string",
                "description": "Description of key4",
                "search": ["full-text"],
                "is_terminal": True
            }
        })



class AttributeNamesTests(TestCase):

    def test_can_get_attribute_names(self):
        schema = {
            "key1": {"is_terminal": True, "search": [1, 2]},
            "key2": {
                "key21": {"is_terminal": True, "search": [3, 4]},
                "key22": {"is_terminal": True, "search": [5, 6]},
                "key23": {
                    "key231": {"is_terminal": True, "search": [7, 8]},
                    "key232": {"is_terminal": True, "search": [9, 10]},
                }
            },
            "key3": {"is_terminal": True, "search": [11, 12]}
        }
        self.assertEqual(get_attribute_names(schema), {
            "key1": [1, 2],
            "key2.key21": [3, 4],
            "key2.key22": [5, 6],
            "key2.key23.key231": [7, 8],
            "key2.key23.key232": [9, 10],
            "key3": [11, 12]
        })