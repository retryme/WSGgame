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

#printRules#
def kural():
    print("Amaç: Koyunu gezdirerek kurta yakalanmadan çimeni yiyebilmek")
    print("Kontroller:")
    print("w= yukarı")
    print("s= aşağı")
    print("a= sola")
    print("d=sağa")
    print("Dikenlere (*) değdiğinizde oyun biter ve kaybedersiniz")
#printRules#


    
#matris oluştur#
for j in range(5):
    for i in range(5):

        table[j-1][i-1] = [j-1,i-1]



#matris oluştur#


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

while grass == ship or wolf ==ship or wolf == grass  :
    wolf[0]= randint(0,3) ###wolf-reassigned until conditions
    wolf[1]= randint(0,3)###wolf-reassigned until conditions
    grass[0]= randint(0,3)###grass-reassigned until conditions
    grass[1]= randint(0,3)###grass-reassigned until conditions
    break


table[ship[0]][ship[1]] = 'Sheep'
table[wolf[0]][wolf[1]] = 'Wolf'
table[grass[0]][grass[1]] = 'Grass'
#ASSİGNMENT TO LİST-END#

kural()
yaz(table)



while True:
    move = input()
    if move == 'w':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        ship = [int(ship[0])-1,ship[1]] ####hareketi tanımlar
        if ship[0] > 3 or ship[1] > 3 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
        else:
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
        
    elif move == 's':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        ship = [int(ship[0])+1,ship[1]] ####hareketi tanımlar
        if ship[0] > 3 or ship[1] > 3 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
        else:
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
        
    elif move == 'a':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        ship = [ship[0],int(ship[1])-1] ####hareketi tanımlar
        if ship[0] > 3 or ship[1] > 3 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
        else:
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
        
    elif move == 'd':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        ship = [ship[0],int(ship[1])+1] ####hareketi tanımlar
        if ship[0] > 3 or ship[1] > 3 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
        else:
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
      











