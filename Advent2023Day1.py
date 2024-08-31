import re

file_path = 'Advent2023Day1.txt'

total_sum = 0

with open(file_path, 'r') as file:
   calibrations = file.readlines()

calibrations = [calibration.strip() for calibration in calibrations]

for calibration in calibrations:
    first_digit_scrape = re.search(r'\d', calibration)

    if first_digit_scrape:
      first_digit = first_digit_scrape.group()
    else: 
      print("ERROR NO FIRST DIGIT FOUND")

    last_digit_scrape = re.findall(r'\d', calibration)

    if last_digit_scrape:
       last_digit = last_digit_scrape[-1]
    else:
       print("ERROR NO SECOND DIGIT FOUND")

    calibration= int(str(first_digit) + str(last_digit))
    print(calibration)
    total_sum += calibration
    print(calibration)

print(f"The Sum of all of the numbers is {total_sum}")