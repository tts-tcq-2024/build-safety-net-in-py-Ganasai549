import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("Z"), "Z000")

    def test_case_insensitivity(self):
        self.assertEqual(generate_soundex("ROBERT"), generate_soundex("robert"))

    def test_vowels(self):
        self.assertEqual(generate_soundex("Aeiou"), "A000")

    def test_consonants(self):
        self.assertEqual(generate_soundex("Bcdghjklmnpqrstvwxyz"), "B232")

if __name__ == '__main__':
    unittest.main()
