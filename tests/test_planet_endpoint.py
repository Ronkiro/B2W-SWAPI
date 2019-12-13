import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from main import app
import json
from mongoengine.errors import ValidationError
class TestPlanetEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_if_GET_method_returns_correct_status_code(self):
        r = self.app.get('/api/planets')
        self.assertEqual(200, r.status_code)

    def test_if_DELETE_method_returns_correct_status_code(self):
        r = self.app.delete('/api/planets/1', method='DELETE')
        self.assertIn(r.status_code, [204, 404])
        r = self.app.delete('/api/planets/DWADWAD', method='DELETE')
        self.assertEqual(404, r.status_code)
        r = self.app.delete('/api/planets', method="DELETE")
        self.assertEqual(400, r.status_code)
    
    def test_if_POST_method_returns_correct_status_code(self):
        r = self.app.post('/api/planets', method='POST', json={ 
                                                                "name": "test", 
                                                                "terrain": "test",
                                                                "climate": "test"
                                                            })
        self.assertEqual(r.status_code, 201)
        with self.assertRaises(ValidationError):
            self.app.post('/api/planets', method='POST', json={ 
                                                            "name": "test", 
                                                            "terrain": "test",
                                                        })
    
    def test_if_GET_returns_correct_data(self):
        r = self.app.get('/api/planets')
        self.assertIsInstance(json.loads(r.data)['data'], str)