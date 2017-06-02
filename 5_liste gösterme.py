
from random import randint

rows_count = 4
cols_count = 4



table= [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


for j in range(5):
    for i in range(5):

        table[j-1][i-1] = (j-1,i-1)

print("************************************")
print("*", table[0],"*")
print("*", table[1],"*")
print("*", table[2],"*")
print("*", table[3],"*")
print("************************************")


ship= [0,0]
ship[0]= randint(0,3)
ship[1]= randint(0,3)
print(ship)
print(int(ship[0]),int(ship[1]))

print(table[ship[0]][ship[1]])
table[ship[0]][ship[1]] = 'Wolf'

print("************************************")
print("*", table[0],"*")
print("*", table[1],"*")
print("*", table[2],"*")
print("*", table[3],"*")
print("************************************")






