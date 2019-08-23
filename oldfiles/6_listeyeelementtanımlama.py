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

#INDEX DEFINITION OF VARIABLES-BEGIN#

#SHEEEEEEEEEEEEP
ship= [0,0]
ship[0]= randint(0,3)
ship[1]= randint(0,3)
#SHEEEEEEEEEEEEP


#WOLFFFFFFFFFFFFFFFFFFFFFF
wolf= [0,0]
wolf[0]= randint(0,3)
wolf[1]= randint(0,3)
#WOLFFFFFFFFFFFFFFFFFFFFFF


#Grassssssssssssssssssssssssss
grass= [0,0]
grass[0]= randint(0,3)
grass[1]= randint(0,3)

#Grassssssssssssssssssssssssss
#INDEX DEFINITION OF VARIABLES-BEGIN#


#ASSİGNMENT TO LİST-BEGIN#
#SHEEEEEEEEEEEEP
while grass == ship or wolf ==ship:
    wolf[0]= randint(0,3)
    wolf[1]= randint(0,3)
    break
print(ship)
#print(int(ship[0]),int(ship[1]))
#print(table[ship[0]][ship[1]])

table[ship[0]][ship[1]] = 'Sheep'

#SHEEEEEEEEEEEEP


#WOLFFFFFFFFFFFFFFFFFFFFFF
while grass == wolf or wolf ==ship:
    wolf[0]= randint(0,3)
    wolf[1]= randint(0,3)
    break
print(wolf)
#print(int(wolf[0]),int(wolf[1]))
#print(table[wolf[0]][wolf[1]])

table[wolf[0]][wolf[1]] = 'Wolf'

#WOLFFFFFFFFFFFFFFFFFFFFFF


#Grassssssssssssssssssssssssss
while grass == wolf or grass ==ship:
    grass[0]= randint(0,3)
    grass[1]= randint(0,3)
    break
print(grass)
#print(int(grass[0]),int(grass[1]))
#print(table[grass[0]][grass[1]])

table[grass[0]][grass[1]] = 'Grass'

#Grassssssssssssssssssssssssss
#ASSİGNMENT TO LİST-END#



print("************************************")
print("*", table[0],"*")
print("*", table[1],"*")
print("*", table[2],"*")
print("*", table[3],"*")
print("************************************")




















