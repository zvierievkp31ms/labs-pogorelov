import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest
from indexfile import index_file

class TestIndexFile(unittest.TestCase):
    def setUp(self):
        self.files = ['input_files/test/file_1.txt', 'input_files/test/file_2.txt']
        self.index = 'results/index'
        self.filenames = 'results/filenames'

    def tearDown(self):
        pass

    def test_indexing_all_exist_files(self):
        result = index_file(self.files, self.index, self.filenames)
        self.assertEqual(result, {'index': 'filenames'})

    def test_indexing_one_not_exist_files(self):
        files = self.files
        files[0] += 'to'
        result = index_file(files, self.index, self.filenames)
        self.assertEqual(result, {'index': 'filenames'})

    def test_indexing_empty_files_array(self):
        result = index_file([], self.index, self.filenames)
        self.assertEqual(result, {'index': 'filenames'})

if __name__ == "__main__":
    unittest.main()