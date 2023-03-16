# Defining a function in Python
# name should be in lower case
# multiple words should be separated using and underscore
def say_hi():
    print("Hello User")


def hi_user_info(name, age):
    print("Hi " + name + ", you are " + str(age))

def cube(num):
    return num * num * num

print("Top")
say_hi()
hi_user_info("John", 20)
hi_user_info("Fuji", 40)

result = cube(3)
print(result)
print("Bottom")
