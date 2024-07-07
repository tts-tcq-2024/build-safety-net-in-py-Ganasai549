import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("Z"), "Z000")

    def test_uppercase_lowercase(self):
        self.assertEqual(generate_soundex("ROBERT"), generate_soundex("robert"))

    def test_vowels(self):
        self.assertEqual(generate_soundex("Aeiou"), "A000")

    def test_consonants(self):
        self.assertEqual(generate_soundex("Bcdghjklmnpqrstvwxyz"), "B232")

    def test_similar_names(self):
        self.assertEqual(generate_soundex("Robert"), generate_soundex("Rupert"))
        self.assertEqual(generate_soundex("Ashcraft"), generate_soundex("Ashcroft"))

    def test_names_with_prefixes(self):
        self.assertEqual(generate_soundex("MacDonald"), generate_soundex("McDonald"))

    def test_names_with_h_and_w(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Williams"), "W452")

    def test_names_with_repeated_letters(self):
        self.assertEqual(generate_soundex("Gutierrez"), "G362")

    def test_names_with_adjacent_letters_same_code(self):
        self.assertEqual(generate_soundex("Jackson"), "J250")

    def test_names_with_different_first_letter(self):
        self.assertNotEqual(generate_soundex("Tymczak"), generate_soundex("Dymczak"))

    def test_long_name(self):
        self.assertEqual(generate_soundex("Wolfeschlegelsteinhausenbergerdorff"), "W412")

    def test_names_with_apostrophes(self):
        self.assertEqual(generate_soundex("O'Brien"), generate_soundex("OBrien"))

    def test_names_with_hyphens(self):
        self.assertEqual(generate_soundex("Mary-Jane"), generate_soundex("MaryyJane"))

    def test_names_with_spaces(self):
        self.assertEqual(generate_soundex("Van der Wal"), generate_soundex("Vanderwal"))

    def test_mixed_case(self):
        self.assertEqual(generate_soundex("MacDoNaLd"), generate_soundex("MaCdOnAlD"))

if __name__ == '__main__':
    unittest.main()
