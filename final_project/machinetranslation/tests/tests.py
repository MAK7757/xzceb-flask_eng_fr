import unittest
import sys
sys.path.append('../')  # Add the parent directory to the Python path

from translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):
    def test_englishToFrench_hello(self):
        english_text = 'hello'
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, 'bonjour')

    def test_frenchToEnglish_bonjour(self):
        french_text = 'Bonjour'
        english_text = french_to_english(french_text)
        self.assertEqual(english_text, 'Hello')

if __name__ == '__main__':
    unittest.main()

