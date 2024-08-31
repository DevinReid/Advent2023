import re

# Define the input string
# input_string = "9lzvbtlkzdgzcxrbtlthhqbdvklgkz7nine1"

file_path = 'Advent2023Day1.txt'

def edit_data():
    with open(file_path, 'r') as file:
        content = file.read()
   
    replacements = {
        'oneight': 'oneeight',
        'twone': 'twoone',
        'eightwo': 'eighttwo',
        'threeight': 'threeeight',
        'fiveight': 'fiveeight',
        'sevenine': 'sevennine',
        'eighthree': 'eightthree',
        'nineight': 'nineeight'
    }

    updated_content = content
    for old, new in replacements.items():
        updated_content = updated_content.replace(old, new)


    with open(file_path, 'w') as file:
        file.write(updated_content)

edit_data()