from random import randint

rows_count = 4
cols_count = 4



table= [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
#printfunction-begin#
def yaz(table):
    print("************************************")
    print("*", table[0],"*")
    print("*", table[1],"*")
    print("*", table[2],"*")
    print("*", table[3],"*")
    print("************************************")
#printfunction-end#


#matris oluştur#
for j in range(5):
    for i in range(5):

        table[j-1][i-1] = (j-1,i-1)

#matris oluştur#

print("our table")
yaz(table)

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
#INDEX DEFINITION OF VARIABLES-END#


#ASSİGNMENT TO LİST-BEGIN#
#SHEEEEEEEEEEEEP
while grass == ship or wolf ==ship:
    wolf[0]= randint(0,3)
    wolf[1]= randint(0,3)
    break
print("ship ",ship)
#print(int(ship[0]),int(ship[1]))
#print(table[ship[0]][ship[1]])

table[ship[0]][ship[1]] = 'Sheep'

#SHEEEEEEEEEEEEP


#WOLFFFFFFFFFFFFFFFFFFFFFF
while grass == wolf or wolf ==ship:
    wolf[0]= randint(0,3)
    wolf[1]= randint(0,3)
    break
print("wolf ",wolf)
#print(int(wolf[0]),int(wolf[1]))
#print(table[wolf[0]][wolf[1]])

table[wolf[0]][wolf[1]] = 'Wolf'

#WOLFFFFFFFFFFFFFFFFFFFFFF


#Grassssssssssssssssssssssssss
while grass == wolf or grass ==ship:
    grass[0]= randint(0,3)
    grass[1]= randint(0,3)
    break
print("grass ", grass)
#print(int(grass[0]),int(grass[1]))
#print(table[grass[0]][grass[1]])

table[grass[0]][grass[1]] = 'Grass'

#Grassssssssssssssssssssssssss
#ASSİGNMENT TO LİST-END#






yaz(table)


while True:
    move = input()
    if move == 'w':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        ship = [int(ship[0])-1,ship[1]] ####hareketi tanımlar
       #table[ship[0]][ship[1]] = 'Sheep' bu işlemi ifelse içinde yapmak lazım
        if ship == grass:
            table[ship[0]][ship[1]] =  'Ship and Grass'
            yaz(table) #print the table
            print("Kazandınız")
            break
        elif ship == wolf:
            table[ship[0]][ship[1]] = 'Ship and Wolf'
            yaz(table) #print the table
            print("kaybettiniz")
            break
        else:
            table[ship[0]][ship[1]] = 'Sheep'
        
        yaz(table)
        #move = input()
    elif move == 's':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        ship = [int(ship[0])+1,ship[1]] ####hareketi tanımlar
        if ship == grass:
            table[ship[0]][ship[1]] =  'Ship and Grass'
            yaz(table) #print the table
            print("Kazandınız")
            break
        elif ship == wolf:
            table[ship[0]][ship[1]] = 'Ship and Wolf'
            yaz(table) #print the table
            print("kaybettiniz")
            break
        else:
            table[ship[0]][ship[1]] = 'Sheep'
        
        yaz(table)
        #move = input()
    elif move == 'a':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        ship = [ship[0],int(ship[1])-1] ####hareketi tanımlar
        if ship == grass:
            table[ship[0]][ship[1]] =  'Ship and Grass'
            yaz(table) #print the table
            print("Kazandınız")
            break
        elif ship == wolf:
            table[ship[0]][ship[1]] = 'Ship and Wolf'
            yaz(table) #print the table
            print("kaybettiniz")
            break
        else:
            table[ship[0]][ship[1]] = 'Sheep'
        
        yaz(table)
        #move = input()
    elif move == 'd':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        ship = [ship[0],int(ship[1])+1] ####hareketi tanımlar
        if ship == grass:
            table[ship[0]][ship[1]] =  'Ship and Grass'
            yaz(table) #print the table
            print("Kazandınız")
            break
        elif ship == wolf:
            table[ship[0]][ship[1]] = 'Ship and Wolf'
            yaz(table) #print the table
            print("kaybettiniz")
            break
        else:
            table[ship[0]][ship[1]] = 'Sheep'
        
        yaz(table)
        #move = input()


















