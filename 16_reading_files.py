# Read from external files
# 2nd prameter "r" indicates that you want to open the file in read only mode
# "w" - open the file in write mode
# "a" - open the file in append mode, only would be able to add new info but not able to change any stored info
# employee_file = open("employee.txt", "r")

# print(employee_file.readable())     # indicates if the file is readable
# print(employee_file.read())     # print all the in the file
# print(employee_file.readline())     # read a line from the file. if this command issues multiple times the cursor
                                    # would move to the next line and prints
# print(employee_file.readlines())     # outputs the file content as a List
# print(employee_file.readlines()[4])     # outputs the file specific line in the List element

# loop through each line in the file
# for employee in employee_file.readlines():
#     print(employee)

# Append to external files
# employee_file = open("employee.txt", "a")

# add an employee to the file
# employee_file.write("\nTom - Human Resources")

# Write to external files
employee_file = open("employee.txt", "w")
employee_file.write("\nKerry - Human Resources")    # The existing contents would be overwritten with this line

employee_file.close();