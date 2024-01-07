import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from io import BytesIO
import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_set_file_for_indexing(self):
        data = dict(file=(BytesIO(b'my file contents'), "work_order.123"))
        response = self.app.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
    
    def test_set_index_file(self):
        data = dict(file=(BytesIO(b'{"asd": [1],"word": [2]}'), "index"))
        response = self.app.post('/index_filenames', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'changes applied', response.data)

    def test_set_filename_file(self):
        data = dict(file=(BytesIO(b'["file_2.txt"]'), "filenames"))
        response = self.app.post('/index_filenames', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'changes applied', response.data)

    def test_empty_query(self):
        response = self.app.get('/query')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: The application cannot process this request, please check the data entered.', response.data)        
    
    def test_query_with_not_exist_value(self):
        response = self.app.get('/query?value=time')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'The word "time" is not found in any of the indexed files.', response.data)        
    
    def test_query_with_value(self):
        response = self.app.get('/query?value=asd')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1 file_2.txt\n', response.data)        
    
if __name__ == "__main__":
    unittest.main()