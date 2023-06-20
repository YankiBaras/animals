from Animals import Animal


class Unicorn(Animal):

    def __init__(self, name, hunger):
        Animal.__init__(self, name)
        self._hunger = hunger

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")
