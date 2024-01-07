import unittest
from indexfile import index_file

class TestIndexFile(unittest.TestCase):
    def setUp(self):
        self.files = ["file_1.txt", "file_2.txt", "file_3.txt"]
    
    def tearDown(self):
        pass
    
    def test_empty_files_array(self):
        result = index_file({})
        self.assertEqual(result, None)

    def test_default_files_array(self):
        res_files = {}
        for file in self.files:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.readlines()
                res_files[file] = content
        result = index_file(res_files)
        self.assertEqual(result['index'], not None)
        self.assertEqual(result['filenames'], not None)

if __name__ == "__main__":
    unittest.main()