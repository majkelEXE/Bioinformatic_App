import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from amino_acid_interpreter.main import check_sequence
from main import MainWindow


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

    def test_5(self):
        self.assertEqual(check_sequence("."), 0, False)

    def test_6(self):
        self.assertEqual(check_sequence("...."), 0, False)

    def test_7(self):
        self.assertEqual(check_sequence("UAGE"), 0, False)


unittest.main()
