import os
import sys
import json
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest
from query import query

class TestIndexFile(unittest.TestCase):
    def test_query_with_not_exist_value(self):
        index = json.load('{"test":[1]}')
        filenames = json.load('["test.file"]')
        word = 'asd'
        response = query(word, index, filenames)
        self.assertEqual(response.status_code, 404)
        self.assertIn(f'The word "{word}" is not found in any of the indexed files.', response.data)        
    
    def test_query_with_not_exist_value(self):
        index = json.load('{"test":[1]}')
        filenames = json.load('["test.file"]')
        word = 'test'
        response = query(word, index, filenames)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1 test.file\n', response.data)     

if __name__ == "__main__":
    unittest.main()