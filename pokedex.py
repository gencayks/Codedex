class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def display_details(self):
        print("Entry: " + str(self.entry))
        print("Name: " + self.name)
        print("Types: " + self.types)
        print("Description: " + self.description)
        print("Is caught: " + str(self.is_caught))

    def speak(self):
        print("Pika Pika!")
pikachu = Pokemon(25, "Pikachu", "Electric ", "This Pokemon has electricity-storing pouches on its cheeks.", False)
pikachu.display_details()
pikachu.speak()

