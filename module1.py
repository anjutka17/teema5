from teema5 import *
#try except
try:
   a=float(input("Arv1: "))
   b=float(input("Arv2: "))
   t=input("Tehe: ")
   vastus=arithmetic(a,b,t)
   print(vastus)
except ValueError:
    print("Viga! Sisestage ainult numbrid!")
vastus==arithmetic(float(input("Arv1: ")),float(input("Arv2: ")),input("Tehe: "))
print(vastus)

aasta=int(input("Mis aasta tahad kontrollida?"))
if aasta>0:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} ei ole liigaasta")

#square() kasutamine
#Kontroll while True ja try except...
#3 

while True:
    try:
        S=float(input("Sisesta ruudu k�lje pikkus: "))
        if S.lower()=="exit":
            print("Programm l�petatud.")
            break
        S=float(input("Sisesta ruudu k�lje pikkus: "))
        S,P,d=square(s)
        print(f"�mberm��t: {P}, Pindala: {S}, Diagonaal {d}")
    except:
        print("Viga, palun uuesti!")
    

#4
while True:
    try:
        param=int(input("Sisesta kuu-(1-12 v�i 'exit' l�petamiseks"))
        if param.lower()=="exit":
            print("Programm l�petatud.")
            break
        param=int(param)
        print("Aastaaeg: ", season(param))
    except:
        print("Viga, sisesta uuesti.")

#5 
while True:
    try:
        summa=input("Sisesta algne sissemakse v�i 'exit' l�petamiseks: ")
        if summa.lower()=="exit":
            print("Programm l�petatud.")
            break
        aasta=input("Sisesta aastate arv: ")
        if aasta.lower()=="exit":
            print("Programm l�petatud.")
            continue
        final_amount=(summa, aasta)
        print(f"P�rast {aasta} aastat on teie kontrol: {final_amount} eurot")
    except:
        print("Viga")

#6
while True:
    try:
        a=input("Sisesta t�isarv: ")
        if a.lower()=="exit":
            print("Viga")
        elif a.lower()=="random":
            print("Jihuslik arv on algarv", is_prime)
        else:
            a=int(a)
            if 1<=a<=1000:
                print(f"{a} on algarv: {is_prime(a)}")
            else:
                print("Viga")
    except:
        print("Viga")
        



#7
while True:
    p�ev=int(input("Sisesta p�ev: "))
    kuu=int(input("Sisesta kuu: "))
    aasta=int(input("Sisesta aasta: "))
    if date(p�ev, kuu, aasta):
        print("Kuup�ev eksisteerib.")
    else:
        print("Vale kuup�ev!")
    v=input("Kas soovid j�tkata? (jah/ei): ")
    if v.lower() != "jah":
        break
