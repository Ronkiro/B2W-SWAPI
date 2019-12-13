import unittest
from resources.SWAPI import SWAPI

class SWAPITestCase(unittest.TestCase):
    def setUp(self):
        self.api = SWAPI()
        self.DAGOBAH_COUNT = 3

    def test_planets(self):
        self.assertIsInstance(self.api.planets(), list)

    def test_find_planet(self):
        self.assertIsInstance(self.api.find_planet('Dagobah'), dict)
        self.assertIsInstance(self.api.find_planet('dagobah'), dict)
        self.assertIsNone(self.api.find_planet('MIDAWDIWJAD'))
        with self.assertRaises(TypeError):
            self.api.find_planet(1)
            self.api.find_planet([])
            self.api.find_planet({})
            
    def test_movie_count(self):
        self.assertIsInstance(self.api.get_movie_count('Dagobah'), int)
        self.assertIsInstance(self.api.get_movie_count('dagobah'), int)
        self.assertEquals(self.api.get_movie_count('MIDAWDIWJAD'), 0)
        with self.assertRaises(TypeError):
            self.api.get_movie_count(1)
            self.api.get_movie_count([])
            self.api.get_movie_count({})
        self.assertEquals(self.api.get_movie_count('Dagobah'), 3)
        self.assertEquals(self.api.get_movie_count('dagobah'), 3)
