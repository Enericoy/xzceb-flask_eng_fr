import unittest
from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):

    def test_frenchtoEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_frenchtoEnglishNotNull(self):
        self.assertIsNotNone(french_to_english('Hello'))

class TestEnglishToFrench(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_englishToFrenchNotNull(self):
        self.assertIsNotNone(english_to_french('Bonjour'))

if __name__ == '__main__':
    unittest.main()