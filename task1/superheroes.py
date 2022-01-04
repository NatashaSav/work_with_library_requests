
class Superheroes:
    def __init__(self, list_of_heroes):
        self.list_of_heroes = list_of_heroes
        for hero in list_of_heroes:
            hero.setup()

    def get_superhero(self):
        self.list_of_heroes.sort()
        return self.list_of_heroes[0]




