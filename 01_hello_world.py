from math import *

# print("Hello World!")

# Drawing a shape
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

# Variables & Data Type
# character_name = "John"
# character_age = 35
# is_male = False
#
# print("There once was a man named " + character_name + ",")
# print("he was " + str(character_age) + " years old.")
# print("He really liked the name " + character_name + ",")
# print("but didn't like being " + str(character_age) + ".")

# Numbers
print(3 * 4 + 5)        # prints 17
print(3 * (4 + 5))      # prints 27

print(10 % 4)           # Modulus operator, prints 2

print(str(10))          # converts to a string

my_num = -5
print(abs(my_num))      # prints 5

print(pow(3, 2))       # prints 9 (power/ square)

print(max(4, 6))        # prints the biggest number

print(min(4, 6))        # prints the smallest number

print(round(3.2))        # rounds and prints 3
print(round(3.7))        # rounds and prints 4

# Below math functions require importing 'math' module
print(floor(3.7))        # get rids of the decimal and prints 3
print(ceil(3.07))        # always rounds up and prints 4
print(sqrt(16))        # square root and prints 4.0


# get input from users
name = input("Enter you name: ")
age = input("Enter you age: ")
print("Hello " + name + " You are " + age)