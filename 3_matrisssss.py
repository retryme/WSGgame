# 2D array/ matrix

# 5 rows, 5 cols
rows_count = 5
cols_count = 5

# create
#     creation looks reverse
#     create an array of "cols_count" cols, for each of the "rows_count" rows
#        all elements are initialized to 0
two_d_array = [[0 for j in range(cols_count)] for i in range(rows_count)]

# index is from 0 to 4
#     for both rows & cols
#     since 5 rows, 5 cols

# use

print(two_d_array)
two_d_array[0][0] = 1
print (two_d_array[0][0])  # prints 1   # 1st row, 1st col (top-left element of matrix)

two_d_array[1][0] = 2
print (two_d_array[1][0])  # prints 2   # 2nd row, 1st col

two_d_array[1][4] = 3
print (two_d_array[1][4])  # prints 3   # 2nd row, last col

two_d_array[4][4] = 4
print (two_d_array[4][4])  # prints 4   # last row, last col (right, bottom element of matrix)
print(two_d_array)
