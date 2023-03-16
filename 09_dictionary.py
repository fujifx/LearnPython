# Dictionary is special structure in Python which allows us to store
# information in what are called key value pairs.
# Essentially you can create a bunch key value pairs and when you want
# to access a specific piece of information in the dictionary
# you refer to it by its key.
# Keys can be either numbers or string as long as they are unique

# This program converts a 3 digits month name to its full name
# eg. Jan -> January

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# print(monthConversions["Nov"])      # Prints November, Search by key
# print(monthConversions.get("Mar"))      # Prints March, Search by key
# print(monthConversions.get("Luv"))      # Prints 'None', since there isn't any match for this key
# print(monthConversions.get("Luv", "Not a valid Key"))      # Prints 'Not a valid Key', default message/ return

