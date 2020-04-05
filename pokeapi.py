import requests
import json
from random import randrange

class PokeAPI(object):

    def __init__(self):
        self.ENDPOINT = 'https://pokeapi.co/api/v2/pokemon'

    def getPokemon(self, x):
        uri = f'{self.ENDPOINT}/{x}'
        r = requests.get(uri)
        data = r.json()
        abilities = data.get('abilities')

        return {
            'name': data.get('name'),
            'image': data.get('sprites', {}).get('front_default'),
            'order': data.get('order'),
            'height': data.get('height'),
            'weight': data.get('weight'),
            'base experience': data.get('base_experience'),
            'area': data.get('location_area_encounters'),
            'species': data.get('species',{}).get('url'),
            'default': data.get('is_default'),
            'types': data.get('types', {}).get([]),
            'abilities': data.get('abilities', {}).get([]),
            'id': data.get('id')

        }


# api = PokeAPI()
# print(json.dumps(api.getPokemon(randrange(10)), indent=2))