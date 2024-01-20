
pg=0
clear = False
while clear != True:
    if pg == 0:
        print(1)
        pg = 3
    elif pg==1:
        print(2)
    elif pg==2:
        print(3)
        pg=4
    elif pg==3:
        print(5)
        pg = 2
    elif pg==4:
        print('f')
        pg=5
    elif pg==5:
        print(6)
        clear= True

print('축하')

a={'d':(930,3)}
def att(mod,modd):
    print(mod)
    print(modd)
print(a['d'][0])
att(a['d'][0])

while a==d: