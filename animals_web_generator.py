import json as js


def load_animals_data(file_path):
    """Load the animals data from JSON file."""
    with open(file_path, "r") as fileobject:
        return js.load(fileobject)


def print_animals_data(animals_data):
    """Print the animals data, only showing existing fields."""
    for animal in animals_data:
        print(f"\nName: {animal.get('name', 'Unknown')}")

        characteristics = animal.get('characteristics', {})

        if 'diet' in characteristics:   # Check if diet exist
            print(f"Diet: {characteristics['diet']}")
        if animal.get('locations'): # Check if location exist
            print(f"Location: {animal['locations'][0]}")
        if 'type' in characteristics:   # Check if type exist
            print(f"Type: {characteristics['type']}")

