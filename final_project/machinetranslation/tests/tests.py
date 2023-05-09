
import unittest
import sys

sys.path.append('../')


from translator import english_to_french,french_to_english

class TestTranslator(unittest.TestCase): 
    def test_englishToFrench(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 2 is given as input the output is 4.
       
        

class TestDouble(unittest.TestCase): 
    def test_frenchToEnglish(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 2 is given as input the output is 4.
       
        
unittest.main()