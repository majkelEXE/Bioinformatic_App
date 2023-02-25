import unittest
from amino_acid_interpreter.main import check_sequence


class tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(check_sequence(
            "tagaggctacacagtcttgaggaaactagaattagaaactaacgctactctcgtctccgtccccgttcttaaaggtaagccgcgtgcactaggtcagcgggcgggatcctcttcgttatcctcccccaaaaggtcttgcggcaccaaggatccccaccataaaactcatgcctatcactagtcgcgactggatgcttataagcgacagcggcctagtgaagggtggtagacaatctcagtgtcttacaaacggtatacctgacctgcgacggctaattacgcactttcaatcttaagttgaggttatcagccggaccaaacactctgtgctcttacttgctgggttccaggagtgcgcgccacgtgaagtcgacaaacttcaaaagcttcgcaggactccacgcagggactccaacggaccttctaacctacccgtgatgtctgctccacgccagctagactcatgccgtcaatgtctggctatattggttaaaagctctcatcaccgtcgatttttttgtggttcgaggccacggctttactagtcccgtaagaccgtggtggtatgggcagcctacgatatgtttagcatcggagaacgtgaagtaaagatattggagatactggacctgattcgatgcactacacaaggccagtctctataggggccctctttgtgtccttagaattacgagcgagattaatgctacaaaggaaagagaaggtcggatgagggtgttagtgacaaatactatgtggtgggccacgaacattacatcacctccacggcacggaggcatggtacgcatatatctttttccctgtttgaccagggggttgatcagacgattcttttgccagtaacagtaacgcgtcagcattgctacgtcatgagtgattcgctagcagaccttgtccacgaataatggcgcacaaactccgcgaacccctcgttcactgaatcaatggttgtgccagcgttggcggtgtgacatacgg"),
            {
                'option1': ['MRVLVTNTMWWATNITSPPRHGGMVRIYLFPCLTRGLIRRFFCQ'],
                'option2': ['MPSMSGYIG', 'MGSLRYV', 'MHYTRPVSIGALFVSLELRARLMLQRKEKVG', 'MAHKLREPLVH'],
                'option3': ['MPITSRDWMLISDSGLVKGGRQSQCLTNGIPDLRRLITHFQS', 'MSAPRQLDSCRQCLAILVKSSHHRRFFCGSRPRLY', 'MFSIGEREVKILEILDLIRCTTQGQSL', 'MSDSLADLVHE', 'MVVPALAV']
            },
            "Wrong result"
        )

    def test_2(self):
        self.assertEqual(check_sequence(
            "AACTGCGGTGGTGGTAGGTTTACAATCCAGCGAGCCGGGCGTCGTACTGATTAGAGCATATAAACCTGGATTAATCAACACCCTTCATCACGGCTCGATTCCATCGGACGGCAGACGAAAGCAGACTGGCTTTTGCGGCACGGGGATATGCGGTAAGCCAGGATAAGAACAACATTTTACTTCGCAAATGACCTGGTGCGCTTTTACGACAATAATAGGTCGTTTTTGGGAAGTCACGGGTCGGCGGATTCGGGATCAGCGGGTTATCTAGATCGGCGCGTTTAGCAAGGGTGCCGCAGGCCGTACTGTACTATTGACACTTAATACCCGTACTAATGGATGAACAGCGTTCTAATACTGTCACGGTA"),
            {
                'option1': ['MR'],
                'option2': ['MTWCAFTTIIGRFWEVTGRRIRDQRVI'],
                'option3': []
            },
            "Wrong result"
        )

    def test_3(self):
        self.assertEqual(check_sequence(""), 0, "Wrong result")

    def test_4(self):
        self.assertEqual(check_sequence("   "), 0, "Wrong result")


unittest.main()
