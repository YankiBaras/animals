from Animals import Animal


class Cat(Animal):

    def __init__(self, name, hunger):
        Animal.__init__(self, name)
        self._hunger = hunger

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")
