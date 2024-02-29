import re
import sys

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

game_pattern_str = r"Game (\d{1,3}): (.*)"
# num_color_pattern_str = r"(\d{1,3}) (\w{1,5})"
num_blue_pattern_str = r"(\d{1,3}) blue"
num_red_pattern_str = r"(\d{1,3}) red"
num_green_pattern_str = r"(\d{1,3}) green"

def is_game_possible(
    num_of_red : int,
    num_of_green : int,
    num_of_blue : int
):
    return num_of_red <= MAX_RED and\
        num_of_green <= MAX_GREEN and\
        num_of_blue <= MAX_BLUE

def get_cubes_number_from_game_str(game_str : str):
    """
    Return: list of cubes numbers [r, g, b]
    """
    res = [0,0,0]

    m = re.search(num_red_pattern_str, game_str)

    if m is not None:
        num_of_red = int(m.group(1))
        res[0] = num_of_red
    
    m = re.search(num_green_pattern_str, game_str)

    if m is not None:
        num_of_green = int(m.group(1))
        res[1] = num_of_green

    m = re.search(num_blue_pattern_str, game_str)

    if m is not None:
        num_of_blue = int(m.group(1))
        res[2] = num_of_blue

    return res

def get_power_of_min_set(game_str_list : list):
    min_red = 0
    min_blue = 0
    min_green = 0
    for game_str in game_str_list:
        [n_red, n_green, n_blue] = get_cubes_number_from_game_str(game_str)
        if n_red > min_red:
            min_red = n_red
        if n_green > min_green:
            min_green = n_green
        if n_blue > min_blue:
            min_blue = n_blue

    return min_red * min_blue * min_green


f = open("input2.txt")

if f is None:
    sys.exit(1)

lines = f.readlines()

total = 0

for line in lines:
    game_m = re.match(game_pattern_str, line)
    if game_m is None:
        print(f"Line {line} does not match game pattern!")
        continue

    num_of_grps = len(game_m.groups())

    grps = game_m.groups()
    # print(len(grps))
    # for grp in grps:
    #     print(grp)

    if num_of_grps != 2:
        print(f"Not all grps found. Parse error in line {line}")
        continue

    game_num = int(grps[0])

    game_possible = True

    all_games_str = grps[1]
    games_str_list = all_games_str.split(";")

    total += get_power_of_min_set(games_str_list)
    
    
print(f"Total: {total}")

