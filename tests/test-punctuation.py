import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest
from indexfile import index_file, remove_punctuation

class TestPunctuation(unittest.TestCase):    
    def test_remove_punctuation_end(self):
        result = remove_punctuation('Hi.')
        self.assertEqual(result, 'hi')
    
    def test_remove_punctuation_start(self):
        result = remove_punctuation('~Hi')
        self.assertEqual(result, 'hi')
    
    def test_remove_punctuation_full(self):
        result = remove_punctuation('~Hi.')
        self.assertEqual(result, 'hi')

if __name__ == "__main__":
    unittest.main()