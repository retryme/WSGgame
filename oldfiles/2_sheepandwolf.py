from random import randint

table=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1]
for i in range (16):
        
    table [i] = i
print(table)



ship = randint(0,15)
print("ship is ",ship)
table[ship-1] = 'Sheep'
print("index of Sheep  is ",table.index('Sheep'))

wolf = randint(0,15)
print("wolf is ",wolf)
table [wolf-1] = 'Wolf'
print("index of Wolf  is ",table.index('Wolf'))

grass = randint(0,15)
print("grass is ",grass)
table [grass-1] = 'Grass'
print("index of grass  is ",table.index('Grass'))

print(table)

#table[ship-1] = ship-1


if table.index('Wolf') == table.index('Grass'):
    print("geçersiz")
elif table.index('Sheep') == table.index('Wolf'):
    print("kaybettiniz")
else:
    while True:
        move = input()
        if move == 'w':
            table[ship-1] = ship-1 # listedeki boşluğu düzeltiyor
            ship = ship-5
            if table[ship-1] == 'Grass':
                table[ship-1] = 'Ship and Grass'
                print(table)
                print("Kazandınız")
                break
            elif table[ship-1] == 'Wolf':
                table[ship-1] = 'Ship and Wolf'
                print(table)
                print("kaybettiniz")
                break
            else:
                table[ship-1] = 'Sheep'
            
            print(table)
            #move = input()
        elif move == 's':
            table[ship-1] = ship-1
            ship = ship +5
            if table[ship-1] == 'Grass':
                table[ship-1] = 'Ship and Grass'
                print(table)
                print("Kazandınız")
                break
            elif table[ship-1] == 'Wolf':
                table[ship-1] = 'Ship and Wolf'
                print(table)
                print("kaybettiniz")
                break
            else:
                table[ship-1] = 'Sheep'
            print(table)
            #move = input()
        elif move == 'a':
            table[ship-1] = ship-1
            ship = ship-1
            if table[ship-1] == 'Grass':
                table[ship-1] = 'Ship and Grass'
                print(table)
                print("Kazandınız")
                break
            elif table[ship-1] == 'Wolf':
                table[ship-1] = 'Ship and Wolf'
                print(table)
                print("kaybettiniz")
                break
            else:
                table[ship-1] = 'Sheep'
            print(table)
            #move = input()
        elif move == 'd':
            table[ship-1] = ship-1
            ship = ship+1
            if table[ship-1] == 'Grass':
                table[ship-1] = 'Ship and Grass'
                print(table)
                print("Kazandınız")
                break
            elif table[ship-1] == 'Wolf':
                table[ship-1] = 'Ship and Wolf'
                print(table)
                print("kaybettiniz")
                break
            else:
                table[ship-1] = 'Sheep'
            print(table)
            #move = input()

    
    
    



    

    
