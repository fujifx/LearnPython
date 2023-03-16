num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

#result = int(num1) + int(num2)      # WARNING this would generate an error if a decimal number is input by the user
result = float(num1) + float(num2)

print(result)