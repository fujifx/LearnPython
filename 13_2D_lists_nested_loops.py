# 2D List
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# print(number_grid[0][0])        # to print 1 from the above 2D list
# print(number_grid[2][1])        # to print 8 from the above 2D list

# Nested Loop

for row in number_grid:
    for col in row:
        print(col)