import os
import json
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_set_empty_file_dir_for_indexing(self):
        data = {
            'dir':'',
            'filenames': 'filenames',
            'index':'index'
        }
        response = self.app.post('/input', content_type='application/json', data = json.dumps(data))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"index":"filenames"}', response.data)
    
    def test_set_bad_file_dir_for_indexing(self):
        data = {
            'dir':'s',
            'filenames': 'filenames',
            'index':'index'
        }
        response = self.app.post('/input', content_type='application/json', data = json.dumps(data))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(b'Error: The application cannot process this request, please check the data entered.', response.data)
    
    def test_set_file_dir_for_indexing(self):
        data = {
            'dir':'art',
            'filenames': 'filenames',
            'index':'index'
        }
        response = self.app.post('/input', content_type='application/json', data = json.dumps(data))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"index":"filenames"}', response.data)
    
    def test_empty_query(self):
        response = self.app.get('/query')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: Not correct index file name, value not exist', response.data)        
    
    def test_not_full_query(self):
        response = self.app.get('/query?value=time&index=index&filenames=')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: Not correct filenames file name', response.data)        
    
    def test_query_with_not_exist_value(self):
        response = self.app.get('/query?value=time1&index=index&filenames=filenames')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'The word "time1" is not found in any of the indexed files.', response.data)   

    def test_query_with_value(self):
        response = self.app.get('/query?value=air&index=index&filenames=filenames')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1 test/file_2.txt\n', response.data)  

if __name__ == "__main__":
    unittest.main()