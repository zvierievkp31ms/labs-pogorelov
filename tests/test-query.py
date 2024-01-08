import os
import sys
import json
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest
from query import query_index

class TestIndexFile(unittest.TestCase):
    def test_query_with_not_exist_value(self):
        index = json.loads('{"test":[1]}')
        filenames = json.loads('["test.file"]')
        word = 'asd'
        response = query_index(word, index, filenames)
        self.assertEqual(response[1], 404)
        self.assertIn(f'The word "{word}" is not found in any of the indexed files.', response[0])        
    
    def test_query_with_exist_value(self):
        index = json.loads('{"test":[1]}')
        filenames = json.loads('["test.file"]')
        word = 'test'
        response = query_index(word, index, filenames)
        self.assertEqual(response[1], 200)
        self.assertIn('1 test.file\n', response[0])

    def test_query_with_empty_value(self):
        index = json.loads('{"test":[1]}')
        filenames = json.loads('["test.file"]')
        word = ''
        response = query_index(word, index, filenames)
        self.assertEqual(response[1], 404)
        self.assertIn('The word "" is not found in any of the indexed files.', response[0])   

if __name__ == "__main__":
    unittest.main()