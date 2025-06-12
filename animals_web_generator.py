import json as js


def load_animals_data(file_path):
    """Load the animals data from JSON file."""
    with open(file_path, "r") as fileobject:
        return js.load(fileobject)

animals_data = load_animals_data('animals_data.json')


