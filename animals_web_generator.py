import json as js


def get_animals_data(file_path):
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


def get_html_data(file_path):
    """Load the data from HTML file."""
    try:
        with open(file_path, "r") as fileobject:
            return fileobject.read()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return ""


def convert_animals_data_to_str(animals_data):
    """Convert the animals data to a string and return it,
     only showing existing fields."""
    animal_output = ""
    for animal in animals_data:
        animal_output += f"Name: {animal.get('name')}\n"

        characteristics = animal.get('characteristics', {})

        if 'diet' in characteristics:   # Check if diet exist
            animal_output += f"Diet: {characteristics['diet']}\n"
        if animal.get('locations'): # Check if location exist
            animal_output += f"Location: {animal['locations'][0]}\n"
        if 'type' in characteristics:   # Check if type exist
            animal_output += f"Type: {characteristics['type']}\n"

        animal_output += "\n" # Space between the animal outputs

    return animal_output


def write_new_animals_html(template_path, output_path, animals_info):
    """Write the animals data to a ne html file."""
    html_template = get_html_data(template_path)
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open(output_path, "w") as fileobject:
        fileobject.write(html_output)