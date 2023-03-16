# In Python, it is accepted that we catch specific error the error
# and not just catch the exception which would end up catching
# any and every error.

try:
    # answer = 10/0
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input!")