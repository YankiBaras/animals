from Animals import Animal


class Dragon(Animal):
    def __init__(self, name, hunger, color="green"):
        Animal.__init__(self, name)
        self._hunger = hunger
        self._color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")

