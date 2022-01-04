import requests


class Hero:
    def __init__(self, name: str):
        self.name = name
        self.intelligence = None
        self.url = 'https://superheroapi.com/api/2619421814940190/search/' + name.replace(' ', '_')

    def setup(self):
        resp = requests.get(self.url)
        for hero in resp.json().get('results'):
            if hero.get('name') == self.name:
                self.intelligence = hero.get('powerstats').get('intelligence')

    def __lt__(self, hero):
        return self.intelligence < hero.intelligence

    def __str__(self):
        name = "Name: {}".format(self.name)
        intelligence = "Intelligence: {}".format(self.intelligence)
        return "{}\n{}\n".format(name, intelligence)
