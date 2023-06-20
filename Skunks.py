from Animals import Animal


class Skunk(Animal):

    def __init__(self, name, hunger, stink_count=6):
        Animal.__init__(self, name)
        self._hunger = hunger
        self._stink_count = stink_count

    def talk(self):
        print("tssss")

    def stink(self):
        print("Dear lord!")
