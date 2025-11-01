from unittest import TestCase
from pdbsearch.query import get_text_parameters

class GetTextParametersTests(TestCase):

    def test_simple_parameter(self):
        self.assertEqual(get_text_parameters("key1", "value1"), {
            "attribute": "key1",
            "operator": "exact_match",
            "value": "value1"
        })
    

    def test_adding_dots(self):
        self.assertEqual(get_text_parameters("key1__attribute", "value1"), {
            "attribute": "key1.attribute",
            "operator": "exact_match",
            "value": "value1"
        })
    

    def test_not_exact_match(self):
        self.assertEqual(get_text_parameters("key1__attribute__not", "value1"), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "exact_match",
            "value": "value1"
        })
    

    def test_in_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__in", ["value1"]), {
            "attribute": "key1.attribute",
            "operator": "in",
            "value": ["value1"]
        })
    

    def test_not_in_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__not__in", ["value1"]), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "in",
            "value": ["value1"]
        })
    

    def test_greater_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__gt", 10), {
            "attribute": "key1.attribute",
            "operator": "greater",
            "value": 10
        })
    

    def test_not_greater_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__not__gt", 10), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "greater",
            "value": 10
        })
    

    def test_less_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__lt", 10), {
            "attribute": "key1.attribute",
            "operator": "less",
            "value": 10
        })
    

    def test_not_less_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__not__lt", 10), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "less",
            "value": 10
        })
    

    def test_greater_or_equal_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__gte", 10), {
            "attribute": "key1.attribute",
            "operator": "greater_or_equal",
            "value": 10
        })
    

    def test_not_greater_or_equal_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__not__gte", 10), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "greater_or_equal",
            "value": 10
        })
    

    def test_less_or_equal_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__lte", 10), {
            "attribute": "key1.attribute",
            "operator": "less_or_equal",
            "value": 10
        })
    

    def test_not_less_or_equal_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__not__lte", 10), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "less_or_equal",
            "value": 10
        })
    

    def test_equals_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__eq", 10), {
            "attribute": "key1.attribute",
            "operator": "equals",
            "value": 10
        })
    

    def test_not_equals_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__not__eq", 10), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "equals",
            "value": 10
        })
    

    def test_contains_words_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__contains_words", "value1"), {
            "attribute": "key1.attribute",
            "operator": "contains_words",
            "value": "value1"
        })
    

    def test_not_contains_words_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__not__contains_words", "value1"), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "contains_words",
            "value": "value1"
        })
    

    def test_contains_phrase_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__contains_phrase", "value1"), {
            "attribute": "key1.attribute",
            "operator": "contains_phrase",
            "value": "value1"
        })
    

    def test_not_contains_phrase_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__not__contains_phrase", "value1"), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "contains_phrase",
            "value": "value1"
        })
    

    def test_exists_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__exists", True), {
            "attribute": "key1.attribute",
            "operator": "exists",
        })
    

    def test_not_exists_operator(self):
        self.assertEqual(get_text_parameters("key1__attribute__not__exists", True), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "exists",
        })
    

    def test_exists_operator_with_false(self):
        self.assertEqual(get_text_parameters("key1__attribute__exists", False), {
            "attribute": "key1.attribute",
            "negation": True,
            "operator": "exists",
        })