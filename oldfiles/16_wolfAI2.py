from random import randint

#rowsandcolumns = int(input("sayıgir"))


rowsandcolumns=6


# Creates a list containing 5 lists, each of 8 items, all set to 0

table = [[0 for x in range(rowsandcolumns)] for y in range(rowsandcolumns)] #dinamik liste yapımı
#print(table)
#printfunction-begin#
def yaz(table,rowsandcolumns):
    
    print("************************************")
    for i in range (rowsandcolumns):
        print("*", table[i],"*")
    
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
for j in range(rowsandcolumns+1):
    for i in range(rowsandcolumns+1):

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
#print("wolf",wolf)
#print("sheep",ship)
#print("grass",grass)

while grass == ship or wolf == ship or wolf == grass  :
    wolf[0]= randint(0,rowsandcolumns-1) ###wolf-reassigned until conditions ÜST SINIRI DÜZELT
    wolf[1]= randint(0,rowsandcolumns-1)###wolf-reassigned until conditions ÜST SINIRI DÜZELT
    grass[0]= randint(0,rowsandcolumns-1)###grass-reassigned until conditions ÜST SINIRI DÜZELT
    grass[1]= randint(0,rowsandcolumns-1)###grass-reassigned until conditions ÜST SINIRI DÜZELT
    #print("dongu")


#print("wolfafter",wolf)
#print("sheepafter",ship)
#print("grassafter",grass)

table[ship[0]][ship[1]] = 'Sheep'
table[wolf[0]][wolf[1]] = 'Wolf'
table[grass[0]][grass[1]] = 'Grass'
#ASSİGNMENT TO LİST-END#

kural()
yaz(table,rowsandcolumns)

##########################################


def wolfposAI(wolfpos,shippos):
    if abs(int(wolfpos[0])-int(shippos[0])) > abs(int(wolfpos[1])-int(shippos[1])): ##x-y ekseni hareketi küçük olana göre hareket et
        
        if int(wolfpos[1])-int(shippos[1]) > 0:

            
            
            wolfpos[1]= int(wolfpos[1])-1

            
            wolfpos = [int(wolfpos[0]),wolfpos[1]] ####hareketi tanımlar   

            print("wolfposition",wolfpos)
            
        elif int(wolfpos[1])-int(shippos[1]) < 0:
            

            wolfpos[1]= int(wolfpos[1])+1
            
            wolfpos = [int(wolfpos[0]),wolfpos[1]] ####hareketi tanımlar   

            print("wolfposition",wolfpos)

        elif int(wolfpos[1])-int(shippos[1]) == 0: 

            if int(wolfpos[0])-int(shippos[0]) > 0:

                wolfpos[0]= int(wolfpos[0])-1

                print("wolfposition",wolfpos)
                
            elif int(wolfpos[0])-int(shippos[0]) < 0:

                wolfpos[0]= int(wolfpos[0])+1

                print("wolfposition",wolfpos)
            
    elif abs(int(wolfpos[0])-int(shippos[0])) < abs(int(wolfpos[1])-int(shippos[1])):##x-y ekseni hareketi küçük olana göre hareket et
                                                  
        if int(wolfpos[0])-int(shippos[0]) > 0:
            
            

            wolfpos[0]= int(wolfpos[0])-1

            wolfpos = [int(wolfpos[0]),wolfpos[1]] ####hareketi tanımlar   

            print("wolfposition",wolfpos)
            
        elif int(wolfpos[0])-int(shippos[0]) < 0:
            
            

            wolfpos[0]= int(wolfpos[0])+1

            wolfpos = [int(wolfpos[0]),wolfpos[1]] ####hareketi tanımlar   

            print("wolfposition",wolfpos)

        elif int(wolfpos[0])-int(shippos[0]) == 0:

            if int(wolfpos[1])-int(shippos[1]) > 0:

                wolfpos[1]= int(wolfpos[1])-1

                print("wolfposition",wolfpos)
                
            elif int(wolfpos[1])-int(shippos[1]) < 0:

                wolfpos[1]= int(wolfpos[1])+1

                print("wolfposition",wolfpos)

    elif abs(int(wolfpos[0])-int(shippos[0])) == abs(int(wolfpos[1])-int(shippos[1])): ##x-y ekseni hareketi eşit durumda rastgele hareket et

            wolfposrandomMove = randint(0,1)
            if wolfposrandomMove == 0:

                if int(wolfpos[0])-int(shippos[0]) > 0:
                    
                    

                    wolfpos[0]= int(wolfpos[0])-1

                    wolfpos = [int(wolfpos[0]),wolfpos[1]] ####hareketi tanımlar   

                    print("wolfposition",wolfpos)
            
                elif int(wolfpos[0])-int(shippos[0]) < 0:
                    
                    

                    wolfpos[0]= int(wolfpos[0])+1

                    wolfpos = [int(wolfpos[0]),wolfpos[1]] ####hareketi tanımlar   

                    print("wolfposition",wolfpos)
                    
            elif wolfposrandomMove == 1:
                
                if int(wolfpos[1])-int(shippos[1]) > 0:
                    
                    

                    wolfpos[1]= int(wolfpos[1])-1

                    wolfpos = [int(wolfpos[0]),wolfpos[1]] ####hareketi tanımlar   

                    print("wolfposition",wolfpos)
            
                elif int(wolfpos[1])-int(shippos[1]) < 0:
                    
                    

                    wolfpos[1]= int(wolfpos[1])+1
                    
                    wolfpos = [int(wolfpos[0]),wolfpos[1]] ####hareketi tanımlar   

                    print("wolfposition",wolfpos)




##########################################
while True:
    move = input("w,a,s,d\n")
    if move == 'w':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        print("wolfposssss",wolf)
        table[wolf[0]][wolf[1]] = wolf # listedeki boşluğu düzeltiyor
        ship = [int(ship[0])-1,ship[1]] ####hareketi tanımlar
        wolfposAI(wolf,ship)
        if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
            break
        else:
            if ship == grass:
                table[ship[0]][ship[1]] =  'Ship and Grass'
                yaz(table,rowsandcolumns) #print the table
                print("Kazandınız")
                break
            elif ship == wolf:
                table[ship[0]][ship[1]] = 'Ship and Wolf'
                yaz(table,rowsandcolumns) #print the table
                print("kaybettiniz")
                break
            else:
                table[ship[0]][ship[1]] = 'Sheep'
                table[wolf[0]][wolf[1]] = 'Wolf'
            
            yaz(table,rowsandcolumns) #print the table
        
    elif move == 's':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        table[wolf[0]][wolf[1]] = wolf # listedeki boşluğu düzeltiyor
        ship = [int(ship[0])+1,ship[1]] ####hareketi tanımlar
        wolfposAI(wolf,ship)
        if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
            break
        else:
            if ship == grass:
                table[ship[0]][ship[1]] =  'Ship and Grass'
                yaz(table,rowsandcolumns) #print the table
                print("Kazandınız")
                break
            elif ship == wolf:
                table[ship[0]][ship[1]] = 'Ship and Wolf'
                yaz(table,rowsandcolumns) #print the table
                print("kaybettiniz")
                break
            else:
                table[ship[0]][ship[1]] = 'Sheep'
                table[wolf[0]][wolf[1]] = 'Wolf'
            
            yaz(table,rowsandcolumns) #print the table

    elif move == 'a':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        table[wolf[0]][wolf[1]] = wolf # listedeki boşluğu düzeltiyor
        ship = [ship[0],int(ship[1])-1] ####hareketi tanımlar
        wolfposAI(wolf,ship)
        if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
            break
        else:
            if ship == grass:
                table[ship[0]][ship[1]] =  'Ship and Grass'
                yaz(table,rowsandcolumns) #print the table
                print("Kazandınız")
                break
            elif ship == wolf:
                table[ship[0]][ship[1]] = 'Ship and Wolf'
                yaz(table,rowsandcolumns) #print the table
                print("kaybettiniz")
                break
            else:
                table[ship[0]][ship[1]] = 'Sheep'
                table[wolf[0]][wolf[1]] = 'Wolf'
            
            yaz(table,rowsandcolumns) #print the table

        
    elif move == 'd':
        table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        table[wolf[0]][wolf[1]] = wolf # listedeki boşluğu düzeltiyor
        ship = [ship[0],int(ship[1])+1] ####hareketi tanımlar
        wolfposAI(wolf,ship)
        if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
            break
        else:
            if ship == grass:
                table[ship[0]][ship[1]] =  'Ship and Grass'
                yaz(table,rowsandcolumns) #print the table
                print("Kazandınız")
                break
            elif ship == wolf:
                table[ship[0]][ship[1]] = 'Ship and Wolf'
                yaz(table,rowsandcolumns) #print the table
                print("kaybettiniz")
                break
            else:
                table[ship[0]][ship[1]] = 'Sheep'
                table[wolf[0]][wolf[1]] = 'Wolf'
            
            yaz(table,rowsandcolumns) #print the table

      











