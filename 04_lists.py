lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim", "Mick", "Phil", "Meg"]
# friends = ["Kevin", 2, false]  # elements can be of any data type

# print(friends)
# print(friends[1])
# print(friends[-1])      # elements from the back
# print(friends[1:])      # this would grab elements from 1 to the end of the list
# print(friends[1:4])     # grab the elements from 1 and up to 4 (excluding 4th element)

# friends.extend(lucky_numbers)   ## add 2 lists together
# print(friends)

# friends.append("Ben")     # add to the end
# friends.insert(1, "Ben")    # add to a specific location in the list
# friends.remove("Jim")       # removes 'Jim' from the list
# friends.clear()     # gets evey single element inside the list
# friends.pop()          # pops (clears) the last element of the list
# print(friends)

# print(friends.index("Phil"))       # to find the index of a given value, an error would be generated if the provided value isn't found

# friends.append("Jim")
# print(friends.count("Jim"))

# friends.sort()
# print(friends)     # sorts the list in ascending order

# lucky_numbers.sort()
# print(lucky_numbers)

# lucky_numbers.reverse()
# print(lucky_numbers)        # to reverse the order of the elements

friends2 = friends.copy()      # copy a list
print(friends2)
