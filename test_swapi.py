import unittest
from resources.SWAPI import SWAPI

class TestSWAPI(unittest.TestCase):
    def setUp(self):
        self.api = SWAPI()
        self.DAGOBAH_COUNT = 3

    def test_if_planets_are_list(self):
        self.assertIsInstance(self.api.planets(), list)

    def test_if_find_planet_instances_are_correct(self):
        self.assertIsInstance(self.api.find_planet('Dagobah'), dict)
        self.assertIsInstance(self.api.find_planet('dagobah'), dict)
        self.assertIsNone(self.api.find_planet('MIDAWDIWJAD'))
    
    def test_if_find_planet_handles_incorrect_usage(self):
        with self.assertRaises(TypeError):
            self.api.find_planet(1)
            self.api.find_planet([])
            self.api.find_planet({})
            
    def test_if_movie_count_is_correct(self):
        self.assertEqual(self.api.get_movie_count('MIDAWDIWJAD'), 0)
        self.assertEqual(self.api.get_movie_count('Dagobah'), 3)
        self.assertEqual(self.api.get_movie_count('dagobah'), 3)

    def test_if_movie_count_instances_are_correct(self):
        self.assertIsInstance(self.api.get_movie_count('Dagobah'), int)
        self.assertIsInstance(self.api.get_movie_count('dagobah'), int)
    
    def test_if_movie_count_handles_incorrect_usage(self):
        with self.assertRaises(TypeError):
            self.api.get_movie_count(1)
            self.api.get_movie_count([])
            self.api.get_movie_count({})

if __name__ == "__main__":
    unittest.main()