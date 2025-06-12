import json as js


def load_animals_data(file_path):
    """Load the animals data from JSON file."""
    with open(file_path, "r") as fileobject:
        return js.load(fileobject)


def print_animals_data(animals_data):
    """This function prints te animals data."""
    animals_data = load_animals_data("animals_data.json")
    for animal in animals_data:
        animal_name = animal['name']
        animal_diet = animal['characteristics']['diet']
        animal_location = animal['locations'][0]
        animal_type = animal['characteristics']['type']
        print(f"\nName: {animal_name}"
              f"\n Diet: {animal_diet}"
              f"\n Location: {animal_location}"
              f"\n Type: {animal_type}")

print_animals_data(load_animals_data("animals_data.json"))

