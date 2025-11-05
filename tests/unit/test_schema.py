from unittest import TestCase
from pdbsearch.schema import get_attribute_names

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