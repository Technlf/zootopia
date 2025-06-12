import json as js


def load_animals_data(file_path):
    """Load the animals data from JSON file."""
    try:
        with open(file_path, "r") as fileobject:
            return js.load(fileobject)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []
    except js.decoder.JSONDecodeError:
        print(f"File {file_path} could not be decoded.")
        return []


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

