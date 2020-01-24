
import requests
from .models import Superhero
url = 'https://akabab.github.io/superhero-api/api//all.json'
def get_superhero():
    """
    Function to consume http request and return a Quote class instance
    """
    response_list = requests.get(url).json()
    superheroes_list = []
    for sups in response_list:
        sup = Superhero(sups.get("images"), sups.get("biography"),sups.get("powerstats"),sups.get("connections"))
        superheroes_list.append(sup)
    return superheroes_list