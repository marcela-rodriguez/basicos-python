
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
Q1=-1
while Q1 not in [1, 2]:
    Q1=int(input("¿Te gusta el amanecer o el anochecer?:\n1:amanecer\n2: anochecer\nrespuesta:"))

    if Q1 == 1:
        Gryffindor=Gryffindor+1
    elif Q1==1:
        Ravenclaw=+1
    elif Q1 ==2:
        Hufflepuff= +1
    elif Q1 ==2:
        Slytherin =+1
    else:
        print("Entrada incorrecta")


print(Gryffindor,Ravenclaw,Hufflepuff,Slytherin)

Q2=-1
while Q2 not in [1, 2, 3, 4]:
    Q2=int(input("Cuando esté muerto, quiero que la gente me recuerde como:\n1) El Bien\n 2) El Grande\n 3) Los sabios\n 4) El audaz\nrespuesta: "))

    if Q2 == 1:
        Hufflepuff=Hufflepuff+2
    elif Q2==2:
        Slytherin=Slytherin+2
    elif Q2 ==3:
        Ravenclaw=Ravenclaw +2
    elif Q2 ==4:
        Gryffindor =Gryffindor +2
    else:
        print("Entrada incorrecta")

print(Gryffindor,Ravenclaw,Hufflepuff,Slytherin) 

Q3=-1
while Q3 not in [1, 2, 3, 4]:
    Q3=int(input("¿Qué tipo de instrumento agrada más a tu oído?:\n1) el violín\n 2) la trompeta\n 3) el piano\n 4) El tambor\nrespueta:"))

    if Q3 == 1:
        Slytherin=Slytherin+4
        
    elif Q3==2:
        Hufflepuff=Hufflepuff+4
    elif Q3 ==3:
        Ravenclaw=Ravenclaw +4
    elif Q3 ==4:
        Gryffindor =Gryffindor +4
    else:
        print("Entrada incorrecta")

print(Gryffindor,Ravenclaw,Hufflepuff,Slytherin)

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
    print("Gryffindor")
if Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
    print("Ravenclaw")
elif Hufflepuff >= Slytherin:
    print("Hufflepuff")
else:
    print("Slytherin")

