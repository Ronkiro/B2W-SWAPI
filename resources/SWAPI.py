import requests
import json

class SWAPI:
    def __request_planets(self, page):
        r = requests.get(f'https://swapi.co/api/planets?page={page}')
        return json.loads(r.content)

    def planets(self):
        """
        Parses a list of planets
        """
        result_list = []
        page = 1
        content = self.__request_planets(page)
        while(1):
            result_list += content['results']
            if content['next'] is None:             # if no next page
                break                               # stop parsing
            page += 1                               # else keep
            content = self.__request_planets(page)
        return result_list

    def find_planet(self, planet):
        """
        Returns data from a planet if it exists, else None
        """
        if not isinstance(planet, str):
            raise TypeError("planet argument must be str.")
        planets = self.planets()
        for _planet in planets:
            if _planet['name'].lower() == planet.lower():
                return _planet
        return None

    def get_movie_count(self, planet):
        """
        Returns the number of times a planet appeared in a movie
        """
        if not isinstance(planet, str):
            raise TypeError("planet argument must be str.")
        planet = self.find_planet(planet)
        if planet:
            return len(planet['films'])
        return 0