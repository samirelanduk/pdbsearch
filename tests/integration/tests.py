from unittest import TestCase
import pdbsearch

class Tests(TestCase):
    
    def test(self):
        codes = pdbsearch.codes()
        self.assertGreater(len(codes), 150_000)