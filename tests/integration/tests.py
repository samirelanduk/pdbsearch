from unittest import TestCase
import pdbsearch

class Tests(TestCase):
    
    def test_default_codes(self):
        codes = pdbsearch.search()
        self.assertEqual(len(codes), 10)
        self.assertTrue(all(len(code) == 4 for code in codes))
    

    def test_limited_codes(self):
        codes = pdbsearch.search(limit=50)
        self.assertEqual(len(codes), 50)
        codes = pdbsearch.search(limit=2)
        self.assertEqual(len(codes), 2)
    

    def test_pagination_starting(self):
        codes0 = pdbsearch.search(limit=10)
        codes10 = pdbsearch.search(start=10, limit=10)
        self.assertEqual(len(set(codes0) & set(codes10)), 0)
        codes5 = pdbsearch.search(start=5, limit=10)
        self.assertEqual(len(set(codes5) & set(codes0)), 5)
        self.assertEqual(len(set(codes5) & set(codes10)), 5)
        self.assertEqual(codes5[0], codes0[5])
    

    def test_all_codes(self):
        codes = pdbsearch.search(limit=None)
        self.assertGreater(len(codes), 150_000)