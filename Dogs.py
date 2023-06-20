from Animals import Animal


class Dog(Animal):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    def talk(self):
        print("woof woof")



    def fetch_stick(self):
        print("There you go, sir!")



