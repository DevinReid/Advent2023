import re

# Define the input string
# input_string = "9lzvbtlkzdgzcxrbtlthhqbdvklgkz7nine1"

file_path = 'Day 1\Advent2023Day1.txt'



with open(file_path, 'r') as file:
   calibrations = file.readlines()
   print('fileopen')
calibrations = [calibration.strip() for calibration in calibrations]

# Define the pattern to match written numbers
pattern = r"one|two|three|four|five|six|seven|eight|nine|\d"
total_value = 0

number_string_list = { "one": '1',
                    "two": '2',
                      "three": '3',
                        "four": '4',
                          "five": '5'
                        , "six": '6',
                          "seven": '7'
                          , "eight":'8',
                            "nine": '9'}


def decode_single_line(calibration):
    found_numbers = re.findall(pattern, calibration)
               

    for i, number in enumerate(found_numbers):
        if number.isdigit():
            pass
            # print(f'{number} is a digit')
        else: 
            found_numbers[i] = str(number_string_list[number])
            # print(f'digit conversion : {number}')

    # print(found_numbers)  

    found_numbers = [int(number) for number in found_numbers]

    if len(found_numbers) < 1:
        print("Warning: Less than two numbers found, skipping this line.")
        return 0

    # print(found_numbers)
    first_value = found_numbers[0]
    last_value = found_numbers[-1]

    final_value = first_value * 10 + last_value
    print(final_value)
    return final_value

for calibration in calibrations:
    

    total_value += decode_single_line(calibration)


print(total_value)