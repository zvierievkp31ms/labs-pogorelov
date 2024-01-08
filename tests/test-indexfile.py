import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest
from indexfile import index_file, remove_punctuation

class TestIndexFile(unittest.TestCase):
    def test_empty_files_array(self):
        result = index_file({}, 'index', 'filenames')
        self.assertEqual(result['index'], {})
        self.assertEqual(result['filenames'], [])

    def test_default_files_array(self):
        res_files = {
            'file_1.txt':'test value',
            'file_2.txt':'the best',
            'file_3.txt':'test best'
        }
        result = index_file(res_files, 'index', 'filenames')
        self.assertEqual(result['index']['value'], [1,0,0])
        self.assertEqual(result['filenames'], ['file_1.txt', 'file_2.txt', 'file_3.txt'])
    
    def test_remove_punctuation(self):
        result = remove_punctuation('~Hi.')
        self.assertEqual(result, 'hi')

if __name__ == "__main__":
    unittest.main()