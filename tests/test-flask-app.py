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

    def test_set_file_dir_for_indexing(self):
        data = {
            'dir':'art',
            'filenames': 'filenames',
            'index':'index'
        }
        response = self.app.post('/input', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'changes applied', response.data)
    
    def test_set_bad_file_dir_for_indexing(self):
        data = {
            'dir':'',
            'filenames': 'filenames',
            'index':''
        }
        response = self.app.post('/input', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(b'Error: The application cannot process this request, please check the data entered.', response.data)

    def test_empty_query(self):
        response = self.app.get('/query')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: The application cannot process this request, please check the data entered.', response.data)        
    
    def test_not_full_query(self):
        response = self.app.get('/query?value=time&index=index&filenames=')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'The word "time" is not found in any of the indexed files.', response.data)        
    
    def test_query_with_not_exist_value(self):
        response = self.app.get('/query?value=time1')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'The word "time" is not found in any of the indexed files.', response.data)        
    
    def test_query_with_value(self):
        response = self.app.get('/query?value=air&index=index&filenames=filenames')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1 art_file_1.txt\n', response.data)        
    
if __name__ == "__main__":
    unittest.main()