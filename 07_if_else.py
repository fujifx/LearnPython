# If Statements and Comparisons
# == equals
# != not equal
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 40, 5))

# Basic If Statement
# is_male = True
# is_tall = False
# display_text = "You are either not male or tall"
#
# if is_male and is_tall:
#     display_text = "You are a tall male"
# elif is_male and not(is_tall):
#     display_text = "You are a short male"
# elif not(is_male) and is_tall:
#     display_text = "You are not a male but tall"
#
#
# print(display_text)