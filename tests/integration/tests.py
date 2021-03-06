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
        # Match
        codes = pdbsearch.search(ligand_name="ZN", sort="-deposited")
        self.assertEqual(codes, [
            "2SOD", "1PPT", "4TLN", "5TLN", "3CPA", "4CPA", "2ATC", "5CPA", "2INS", "7TLN"
        ])

        # List
        codes = pdbsearch.search(ligand_name__in=["FE", "ZN"], sort="-deposited")
        self.assertEqual(codes, [
            "1HRB", "2SOD", "1PPT", "4TLN", "5TLN", "3CPA", "4CPA", "2ATC", "5CPA", "2INS"
        ])

        # Full
        codes = pdbsearch.search(rcsb_nonpolymer_instance_feature_summary__comp_id="ZN", sort="-deposited")
        self.assertEqual(codes, [
            "2SOD", "1PPT", "4TLN", "5TLN", "3CPA", "4CPA", "2ATC", "5CPA", "2INS", "7TLN"
        ])

        # Full List
        codes = pdbsearch.search(rcsb_nonpolymer_instance_feature_summary__comp_id__in=["FE", "ZN"], sort="-deposited")
        self.assertEqual(codes, [
            "1HRB", "2SOD", "1PPT", "4TLN", "5TLN", "3CPA", "4CPA", "2ATC", "5CPA", "2INS"
        ])
    

    def test_filter_pdbs_by_ligand_distance(self):
        # Match
        codes = pdbsearch.search(ligand_distance=5, sort="-deposited")
        self.assertEqual(codes, [
            "1C1P", "1EM6", "3DN0", "3G0T", "3A0H", "2WSE", "3KZI", "4V6M", "3SEQ", "4IXQ"
        ])

        # Less than
        codes = pdbsearch.search(ligand_distance__lt=5, sort="-deposited")
        self.assertEqual(codes, [
            "1MBN", "2DHB", "3LDH", "2CHA", "2CNA", "1HIP", "1GPD", "1EST", "1CYC", "155C"
        ])

        # Less than equal
        codes = pdbsearch.search(ligand_distance__lte=5, sort="-deposited")
        self.assertEqual(codes, [
            "1MBN", "2DHB", "3LDH", "2CHA", "2CNA", "1HIP", "1GPD", "1EST", "1CYC", "155C"
        ])

        # More than
        codes = pdbsearch.search(ligand_distance__gt=5, sort="-deposited")
        self.assertEqual(codes, [
            "6IY5", "6T52", "6T54", "6T53", "6T58"
        ])

        # More than equal
        codes = pdbsearch.search(ligand_distance__gte=5, sort="-deposited")
        self.assertEqual(codes, [
            "1C1P", "1EM6", "3DN0", "3G0T", "3A0H", "2WSE", "3KZI", "4V6M", "3SEQ", "4IXQ"
        ])

        # Range
        codes = pdbsearch.search(ligand_distance__within=[4, 5], sort="-deposited")
        self.assertEqual(codes, [
            "1GPD", "1EST", "2YHX", "1C4S", "1MBS", "1HDS", "5LDH", "1BP2", "1FC2", "1HBS"
        ])

        # Full
        codes = pdbsearch.search(rcsb_ligand_neighbors__distance=5, sort="-deposited")
        self.assertEqual(codes, [
            "1C1P", "1EM6", "3DN0", "3G0T", "3A0H", "2WSE", "3KZI", "4V6M", "3SEQ", "4IXQ"
        ])
    

    def test_multiple_criteria_searching(self):
        codes = pdbsearch.search(ligand_name="ZN", ligand_distance__within=[2.7, 2.9], sort="-deposited")
        self.assertEqual(codes, [
            "4TLN", "5TLN", "4CPA", "5ADH", "6ADH", "1TLP", "8ATC", "3AT1", "8AT1", "7AT1"
        ])
    

    def test_all_codes(self):
        codes = pdbsearch.search(limit=None)
        self.assertGreater(len(codes), 150_000)