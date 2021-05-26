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
    

    def test_sorting_shorthand(self):
        codes = pdbsearch.search(sort="-deposited")
        self.assertEqual(codes, [
            "1SBT", "1MBN", "2DHB", "3LDH", "2CHA", "3LYZ", "4LYZ", "6LYZ", "5LYZ", "2LYZ"
        ])
        codes = pdbsearch.search(sort="-released")
        self.assertEqual(codes, [
            "1SRX", "1REI", "1MBN", "1EST", "1FDH", "155C", "2PGK", "2SBT", "1CYC", "3CNA"
        ])
        codes = pdbsearch.search(sort=["code", "released"])
        self.assertEqual(codes[0][0], "9")
    

    def test_sorting_full_property(self):
        codes = pdbsearch.search(sort="-rcsb_accession_info.deposit_date")
        self.assertEqual(codes, [
            "1SBT", "1MBN", "2DHB", "3LDH", "2CHA", "3LYZ", "4LYZ", "6LYZ", "5LYZ", "2LYZ"
        ])
        codes = pdbsearch.search(sort="-rcsb_accession_info.initial_release_date")
        self.assertEqual(codes, [
            "1SRX", "1REI", "1MBN", "1EST", "1FDH", "155C", "2PGK", "2SBT", "1CYC", "3CNA"
        ])
    

    def test_filter_pdbs_by_ligand_name(self):
        codes = pdbsearch.search(ligand_name="ZN", sort="-deposited")
        self.assertEqual(codes, [
            "2SOD", "1PPT", "4TLN", "5TLN", "3CPA", "4CPA", "2ATC", "5CPA", "2INS", "7TLN"
        ])
    

    def test_all_codes(self):
        codes = pdbsearch.search(limit=None)
        self.assertGreater(len(codes), 150_000)