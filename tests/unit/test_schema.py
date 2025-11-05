from unittest import TestCase
from unittest.mock import patch
from pdbsearch.schema import *

class DownloadRCSBSchemaTests(TestCase):

    @patch("requests.get")
    @patch("pdbsearch.schema.parse_rcsb_schema")
    def test_can_download_schema_from_url(self, mock_parse, mock_get):
        schema = download_rcsb_schema("https://schema.com")
        self.assertEqual(schema, mock_parse.return_value)
        mock_parse.assert_called_once_with(mock_get.return_value.json.return_value)
        mock_get.assert_called_once_with("https://schema.com")
    

    @patch("requests.get")
    @patch("pdbsearch.schema.parse_rcsb_schema")
    def test_can_download_structure_schema(self, mock_parse, mock_get):
        schema = download_rcsb_schema("structure")
        self.assertEqual(schema, mock_parse.return_value)
        mock_parse.assert_called_once_with(mock_get.return_value.json.return_value)
        mock_get.assert_called_once_with(STRUCTURE_ATTRIBUTES_URL)
    

    @patch("requests.get")
    @patch("pdbsearch.schema.parse_rcsb_schema")
    def test_can_download_chemical_schema(self, mock_parse, mock_get):
        schema = download_rcsb_schema("chemical")
        self.assertEqual(schema, mock_parse.return_value)
        mock_parse.assert_called_once_with(mock_get.return_value.json.return_value)
        mock_get.assert_called_once_with(CHEMICAL_ATTRIBUTES_URL)



class ParseRCSBSchemaTests(TestCase):

    def test(self):
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
        self.assertEqual(parse_rcsb_schema(schema), {
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
            "key1": {"is_terminal": True},
            "key2": {
                "key21": {"is_terminal": True},
                "key22": {"is_terminal": True},
                "key23": {
                    "key231": {"is_terminal": True},
                    "key232": {"is_terminal": True},
                }
            },
            "key3": {"is_terminal": True}
        }
        self.assertEqual(get_attribute_names(schema), [
            "key1",
            "key2.key21",
            "key2.key22",
            "key2.key23.key231",
            "key2.key23.key232",
            "key3",
        ])