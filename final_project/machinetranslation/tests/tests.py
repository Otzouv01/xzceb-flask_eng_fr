"""
Test Module for testing Functions in translator.py
The imported functions are: french_to_english, english_to_french.
Purpose is to compare expected outputs to function outputs.
"""
import unittest
from translator import french_to_english, english_to_french
class TestTranslator(unittest.TestCase):
    """
    TestClass for Module translator.py
    """
    def test_french_to_english(self):
        """
        Test Function for french_to_english function.
        Test Case inputs defined are: Bonjour and Je suis.
        """
        if self is None:
            print('variable is null')
        elif self =='':
            print('variable is null')
        else:
            self.assertEqual(french_to_english('Bonjour'),
            'Hello')
            self.assertEqual(french_to_english('Je suis'),
            'I am')
    def test_english_to_french(self):
        """
        Test Function for english_to_french function. Test Case inputs defined are: I am and Night.
        """
        if self is None:
            print('variable is null')
        elif self =='':
            print('variable is null')
        else:
            self.assertEqual(english_to_french('I am'),
            'Je suis')
            self.assertEqual(english_to_french('Night'),
            'Nuit')
if __name__ == '__main__':
    unittest.main()
