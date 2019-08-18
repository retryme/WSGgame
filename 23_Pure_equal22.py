from random import randint

rowsandcolumns = int(input("sayıgir"))

#comment
#rowsandcolumns=6


# tüm elemanları 0 olan array oluşturur

table = [[0 for x in range(rowsandcolumns)] for y in range(rowsandcolumns)] #dinamik liste yapımı

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
    print("q=yukarı-sol")
    print("e=yukarı-sağ")
    print("z=aşağı-sol")
    print("c=aşağı-sağ")
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
ship[0]= randint(0,rowsandcolumns-1)
ship[1]= randint(0,rowsandcolumns-1)
#SHEEEEEEEEEEEEP


#WOLFFFFFFFFFFFFFFFFFFFFFF
wolf= [0,0]
wolf[0]= randint(0,rowsandcolumns-1)
wolf[1]= randint(0,rowsandcolumns-1)
#WOLFFFFFFFFFFFFFFFFFFFFFF


#Grassssssssssssssssssssssssss
grass= [0,0]
grass[0]= randint(0,rowsandcolumns-1)
grass[1]= randint(0,rowsandcolumns-1)

#Grassssssssssssssssssssssssss
#INDEX DEFINITION OF VARIABLES-END#


#ASSİGNMENT TO LİST-BEGIN#

while grass == ship or wolf == ship or wolf == grass  :
    wolf[0]= randint(0,rowsandcolumns-1) ###wolf-reassigned until conditions 
    wolf[1]= randint(0,rowsandcolumns-1)###wolf-reassigned until conditions 
    grass[0]= randint(0,rowsandcolumns-1)###grass-reassigned until conditions 
    grass[1]= randint(0,rowsandcolumns-1)###grass-reassigned until conditions 

table[ship[0]][ship[1]] = 'Sheep'
table[wolf[0]][wolf[1]] = 'Wolf'
table[grass[0]][grass[1]] = 'Grass'
#ASSİGNMENT TO LİST-END#



##########################################


def wolfposAI(wolfpos,shippos,graspos):

    
    if abs(int(wolfpos[0])-int(shippos[0])) > abs(int(wolfpos[1])-int(shippos[1])): ##x-y ekseni hareketi küçük olana göre hareket et
        
        if int(wolfpos[1])-int(shippos[1]) > 0:

            wolfpos[1]= int(wolfpos[1])-1

            if wolfpos == graspos:

                wolfpos[1] = int(wolfpos[1])+1
                
            
        elif int(wolfpos[1])-int(shippos[1]) < 0:
            
            wolfpos[1]= int(wolfpos[1])+1

            if wolfpos == graspos:

                wolfpos[1] = int(wolfpos[1])-1

        elif int(wolfpos[1])-int(shippos[1]) == 0: 

            if int(wolfpos[0])-int(shippos[0]) > 0:

                wolfpos[0]= int(wolfpos[0])-1

                if wolfpos == graspos:

                    wolfpos[0] = int(wolfpos[0])+1
                
            elif int(wolfpos[0])-int(shippos[0]) < 0:

                wolfpos[0]= int(wolfpos[0])+1

                if wolfpos == graspos:

                    wolfpos[0] = int(wolfpos[0])-1
            
    elif abs(int(wolfpos[0])-int(shippos[0])) < abs(int(wolfpos[1])-int(shippos[1])):##x-y ekseni hareketi küçük olana göre hareket et
                                                  
        if int(wolfpos[0])-int(shippos[0]) > 0:
            
            wolfpos[0]= int(wolfpos[0])-1

            if wolfpos == graspos:

                wolfpos[0] = int(wolfpos[0])+1  
            
        elif int(wolfpos[0])-int(shippos[0]) < 0:

            wolfpos[0]= int(wolfpos[0])+1

            if wolfpos == graspos:

                wolfpos[0] = int(wolfpos[0])-1

        elif int(wolfpos[0])-int(shippos[0]) == 0:

            if int(wolfpos[1])-int(shippos[1]) > 0:

                wolfpos[1]= int(wolfpos[1])-1

                if wolfpos == graspos:

                    wolfpos[1] = int(wolfpos[1])+1
                
            elif int(wolfpos[1])-int(shippos[1]) < 0:

                wolfpos[1]= int(wolfpos[1])+1

                if wolfpos == graspos:

                    wolfpos[1] = int(wolfpos[1])-1

    elif abs(int(wolfpos[0])-int(shippos[0])) == abs(int(wolfpos[1])-int(shippos[1])): ##x-y ekseni hareketi eşit durumda rastgele hareket et

            wolfposrandomMove = randint(0,1)
            if wolfposrandomMove == 0:

                if int(wolfpos[0])-int(shippos[0]) > 0:
                    
                    wolfpos[0]= int(wolfpos[0])-1

                    if wolfpos == graspos:

                        wolfpos[0] = int(wolfpos[0])+1
            
                elif int(wolfpos[0])-int(shippos[0]) < 0:
                    
                    

                    wolfpos[0]= int(wolfpos[0])+1

                    if wolfpos == graspos:

                        wolfpos[0] = int(wolfpos[0])-1
                    
            elif wolfposrandomMove == 1:
                
                if int(wolfpos[1])-int(shippos[1]) > 0:
                    
                    wolfpos[1]= int(wolfpos[1])-1

                    if wolfpos == graspos:

                        wolfpos[1] = int(wolfpos[1])+1
            
                elif int(wolfpos[1])-int(shippos[1]) < 0:
                    
                    wolfpos[1]= int(wolfpos[1])+1
                    
                    if wolfpos == graspos:

                        wolfpos[1] = int(wolfpos[1])-1


#shipmpvement##########################################################
#wwwwwwwwwwwwwwwwww#
def W(north):

    north[0]= int(north[0])-1
    
    print("northhhh",north)
    return north


#wwwwwwwwwwwwwwwwww#

    
#sssssssssssssssssss#
def S(south):

    south[0] = int(south[0])+1

    return south
#sssssssssssssssssss#

#aaaaaaaaaaaaaaaaaaa#
def A(west):

    west[1] = int(west[1])-1

    return west

    
#aaaaaaaaaaaaaaaaaaa#

#ddddddddddddddddddd#
def D(east):

    east[1] = int(east[1])+1

    return east
#ddddddddddddddddddd#



#shipmpvement##########################################################


'''
problem1:
ship ve wolf hareketi fonksiyon içinde tanımlandığı zaman geçmiş konumlarına hep güncel konumlarına yazıyor bundan kaçınmak için

k = wolf[0] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
l = wolf[1]# listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?

m = ship[0]
n = ship[1]

gibi bir işlem yapmak zorunda kaldım ve problem çözüldü. Ancak sebebini bilmiyorum.

Problem2:
bu versiyonda çapraz hareketler tanımlandı ancak wolf == grass konusu çözümlenmedi. Bunu çözmek için wolf-sheep pozisyonu üzerinden bir çözüm gerekebilir.

Çözüldü: bu durumda wolf pozisyonu sabit tutuluyor

'''

kural()
yaz(table,rowsandcolumns)                

##########################################
while True:
    move = input("w,a,s,d,q,e,z,c\n")
    if move == 'w':
        
        k = wolf[0] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        l = wolf[1]# listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        table[wolf[0]][wolf[1]] = [k,l] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        m = ship[0]
        n = ship[1]
        table[ship[0]][ship[1]] = [m,n]
        W(ship)
        print("shippppp",ship)
        wolfposAI(wolf,ship,grass)
        if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
            break
        else:
            if ship == grass:
                table[ship[0]][ship[1]] =  'Ship and Grass'
                table[wolf[0]][wolf[1]] = 'Wolf' 
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
        k = wolf[0] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        l = wolf[1]# listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        table[wolf[0]][wolf[1]] = [k,l] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        S(ship)
        wolfposAI(wolf,ship,grass)
        if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
            break
        else:
            if ship == grass:
                table[ship[0]][ship[1]] =  'Ship and Grass'
                table[wolf[0]][wolf[1]] = 'Wolf'
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
        k = wolf[0] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        l = wolf[1]# listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        table[wolf[0]][wolf[1]] = [k,l] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        A(ship)
        wolfposAI(wolf,ship,grass)
        if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
            break
        else:
            if ship == grass:
                table[ship[0]][ship[1]] =  'Ship and Grass'
                table[wolf[0]][wolf[1]] = 'Wolf'
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
        k = wolf[0] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        l = wolf[1]# listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        table[wolf[0]][wolf[1]] = [k,l] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        D(ship)
        wolfposAI(wolf,ship,grass)
        if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
            break
        else:
            if ship == grass:
                table[ship[0]][ship[1]] =  'Ship and Grass'
                table[wolf[0]][wolf[1]] = 'Wolf'
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

      
    elif move == 'e':
            #table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
            k = wolf[0] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
            l = wolf[1]# listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
            table[wolf[0]][wolf[1]] = [k,l] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
            m = ship[0]
            n = ship[1]
            table[ship[0]][ship[1]] = [m,n]
            W(ship)
            D(ship)
            wolfposAI(wolf,ship,grass)
            if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
                print("dikenlere yakalandınız ve kaybettiniz")
                break
            else:
                if ship == grass:
                    table[ship[0]][ship[1]] =  'Ship and Grass'
                    table[wolf[0]][wolf[1]] = 'Wolf'
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

    elif move == 'q':
            #table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
            k = wolf[0] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
            l = wolf[1]# listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
            table[wolf[0]][wolf[1]] = [k,l] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
            m = ship[0]
            n = ship[1]
            table[ship[0]][ship[1]] = [m,n]
            W(ship)
            A(ship)
            wolfposAI(wolf,ship,grass)
            if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
                print("dikenlere yakalandınız ve kaybettiniz")
                break
            else:
                if ship == grass:
                    table[ship[0]][ship[1]] =  'Ship and Grass'
                    table[wolf[0]][wolf[1]] = 'Wolf'
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


    elif move == 'z':
        #table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        k = wolf[0] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        l = wolf[1]# listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        table[wolf[0]][wolf[1]] = [k,l] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        m = ship[0]
        n = ship[1]
        table[ship[0]][ship[1]] = [m,n]
        S(ship)
        A(ship)
        wolfposAI(wolf,ship,grass)
        if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
            break
        else:
            if ship == grass:
                table[ship[0]][ship[1]] =  'Ship and Grass'
                table[wolf[0]][wolf[1]] = 'Wolf'
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

    elif move == 'c':
        #table[ship[0]][ship[1]] = ship # listedeki boşluğu düzeltiyor
        k = wolf[0] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        l = wolf[1]# listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        table[wolf[0]][wolf[1]] = [k,l] # listedeki boşluğu düzeltiyorWOlf için ama neden shipten farklı?!?!?!?!??!?!?!?!?
        m = ship[0]
        n = ship[1]
        table[ship[0]][ship[1]] = [m,n]
        S(ship)
        D(ship)
        wolfposAI(wolf,ship,grass)
        if ship[0] > rowsandcolumns-1 or ship[1] > rowsandcolumns-1 or ship[0] < 0 or ship[1] < 0 :
            print("dikenlere yakalandınız ve kaybettiniz")
            break
        else:
            if ship == grass:
                table[ship[0]][ship[1]] =  'Ship and Grass'
                table[wolf[0]][wolf[1]] = 'Wolf'
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










