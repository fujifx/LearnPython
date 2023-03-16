import random

feet_in_mile = 5280
meters_in_kilometer = 1000
sahabas = ["Abubucker", "Omar bin Kattab", "Ali ibn Abu Talib", "Usman ibn Affan"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)