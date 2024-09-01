import re

# Your input string game = "Game 1: 1 green, 6 blue, 8 red; 1 green, 1 blue, 1 red; 4 green, 3 blue, 1 red; 4 green, 2 blue, 1 red; 3 blue, 3 green"

file_path = 'Day 2\day2data.txt'

with open(file_path, 'r') as file:
    game_rounds = file.readlines()


print(game_rounds)
total_score = 0
total_power = 0

# Define a regular expression pattern to capture the numbers and colors
pattern = r'(\d+)\s(\w+)'
pattern_two = r'(\d+)'
drop_pattern = r'(\w+\s\d+:)'



def fetch_game_number(game):
    match_two = re.search(pattern_two, game)
    first_number = None

    if match_two:
        first_number = int(match_two.group(1))



    # drop_title_match = re.search(drop_pattern, game)

    # print (game)
    # print("")

    # if drop_title_match:
    #     print(drop_title_match)
    #     game = re.sub(drop_pattern, '', game).strip()
    #     print(game)
    # else:
    #     print("no match")






    # Find all matches in the string
    matches = re.findall(pattern, game)
    print(matches)
    # Initialize variables
    blue = []
    red = []
    green = []

    # Iterate over the matches and assign values to variables
    for match in matches:
        number, color = match
        if color == 'blue':
            blue.append(int(number))
        elif color == 'red':
            red.append(int(number))
        elif color == 'green':
            green.append(int(number))

    for value in blue:
        if value <= 14:
            pass
        else:
            first_number = 0
        
        

    for value in red:
        if value > 12:
            first_number = 0

    for value in green:
        if value > 13:
            first_number = 0

    lowest_blue = max(blue)
    lowest_red = max(red)
    lowest_green = max(green)
    print(f'min blue {lowest_blue}, min green {lowest_green}, min red {lowest_red}')
    power = lowest_blue * lowest_green * lowest_red
    print(f'power = {power}')
    

    print(f"blue = {blue}")
    print(f"red = {red}")
    print(f'green = {green}')
    print(f"Game_number = {first_number}")
    return first_number, power


for game in game_rounds:
    first_number, power = fetch_game_number(game)

    total_score += first_number
    total_power += power
print(total_score)
print(total_power)