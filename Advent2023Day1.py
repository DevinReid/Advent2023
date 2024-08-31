import re

file_path = 'Advent2023Day1.txt'

total_sum = 0

with open(file_path, 'r') as file:
   calibrations = file.readlines()

calibrations = [calibration.strip() for calibration in calibrations]

number_string_list = {"one": 1,
                    "two": 2,
                      "three": 3,
                        "four": 4,
                          "five": 5
                        , "six": 6,
                          "seven": 7
                          , "eight":8,
                            "nine": 9}


for calibration in calibrations:
    first_digit_scrape = re.search(r'\d', calibration)
    first_string_scrape = None
    first_string_position = None

    for number in number_string_list:
       match =re.search(number, calibration)
       if match:
          first_string_scrape = number_string_list[number]
          first_string_position = match.start()
          break
    print(f'first Digit: {int(first_digit_scrape.group())}      First String: {first_string_scrape}')   
    first_digit = None
    if first_digit_scrape and (first_string_scrape is not None):
        if first_digit_scrape.start() < first_string_position:
          first_digit = int(first_digit_scrape.group())
        else:
           first_digit = first_string_scrape
    elif first_digit_scrape:
       first_digit = int(first_digit_scrape.group())
    elif first_string_scrape is not None:
       first_digit = first_string_scrape
    else:
       print("error: no digit or number word found")
       
        

    last_digit_scrape = re.findall(r'\d', calibration)
    last_string_scrape = None
    last_string_position = None
    last_digit = None
 
    for number in number_string_list:
       match = list(re.finditer(number, calibration))
       if match:
          last_match = match[-1]
          last_string_scrape = number_string_list[number]
          last_string_position = last_match.start()
    print(f'Last Digit: {int(last_digit_scrape[-1])}      Last String: {last_string_scrape}')
    if last_digit_scrape and (last_string_scrape is not None):
        
        last_digit_position = len(calibration) - calibration[::-1].index(last_digit_scrape[-1]) - 1
        if last_digit_position > last_string_position:
          last_digit = int(last_digit_scrape[-1])
        else:
           last_digit = last_string_scrape
    elif last_digit_scrape:
       last_digit = int(last_digit_scrape[-1])
    elif last_string_scrape is not None:
       last_digit = last_string_scrape
    else:
       print("ERROR NO SECOND DIGIT FOUND")

    calibration= int(str(first_digit) + str(last_digit))

    print(f'First Number: {first_digit}        Last Number: {last_digit}      Total Number:{calibration}')
    total_sum += calibration


print(f"The Sum of all of the numbers is {total_sum}")
