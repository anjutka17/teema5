#Ulesanne 1
def arithmetic(arv1:float,arv2:float,tehe:str)-> any:
    """Funktsioon t��tab nagu lihtne kalkulaator
    + - liitmine,
    - - lahutamine,
    * - korrutamine
    / - jagamine
    Kui sisend pole j�rjendis [+,-,/,*],siis tagastab s�ne "Tundmatu tehe"
    :param float arv1: Sisend ujukomaarvu t��bina 
    :param float arv2: Sisend ujukomaarvu t��bina
    :param str tehe: Sisesnd listist [+,-,/,*]
    :rtype:varM��remata t��p (float v�i str)
    """
    if tehe in ["+","-","/","*"]:
        if arv2==0 and tehe=="/":
            vastus="VIGA"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus

def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True,kui aasta on liigaasta ja False kui aasta on tavaline aasta
    :param int aasta:Sisend kasutajalt
    :rtype: bool t�ev��rsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v
#3
def square(k�lg:float)->any:
    """Funktsioon leiab
   Ruudu �mberm��tu
   Ruudu pindala
   Ruudu diagonaal
   :param float S: Sisend ujukomaarv
   :param float P: Sisend ujukomaarv
   :param float d: Sisend ujukomaarv
   :rtype:t��p (float)
    """
    S=k�lg**2
    P=4*k�lg
    d=(2)**(1/2)*k�lg
    return S,P,d
#4
def season(param:int)->str:
    """Funktsioon leiab
    Talv - [1,2,12]
    Kevad - [3,4,5]
    Suvi - [6,7,8]
    S�gi - (else kuu)
    :param in range (1,12)
    :rtype: t��p Talv, Kevad, Suvi, S�gi 
    """
    if param in [1,2,12]:
        H="Talv"
    elif param in [3,4,5]:
        H="Kevad"
    elif param in [6,7,8]:
        H="Suvi"
    else:
        H="S�gi"
    return H
#5
def bank(summa:float, aastad:int)->float:
    """Funktsioon leiab panus
    Igal aastal suureneb tema panuse suurus 10%
    :param aasta: Aastate arv, millle jooksul raha hoiatakse 
    :param summa Esialgune sissemaks (eurodes)
    :rtype: t��p(int v�i float)
    """

    for aasta in range(aastad):
        summa*=1.1
        return summa

#6
from random import *
def is_prime(a=randint(1,1000))->bool:
    """Funktisioon kontrollib, kas antud arv v�i algarv
    :param a: T�isarv vahemikus 0 kuni 1000
    :rtype:True, kui a on algarv, vastasel juhul False
    """
    print(a)
    v=True        
    for jagaja in range(2,a):
        if a%jagaja==0:
             v=False
        return v

#7
def date (p�ev:int, kuu:int, aasta:int)->bool:
    """Funktsioon kontrollib, kas kuup�ev eksisteerib kalendaris
    :param day: p�ev (t�isarv)
    :param mounth: Kuu (t�isarv)
    :param year: aasta (t�isarv)
    :rtupe: bool
    """
    if p�ev in range(1,32) and kuu in[1,3,5,7,8,10,12] and aasta>0:
        v=True
    elif p�ev in range (1,30) and kuu==2 and is_year_leap(aasta):
        v=True
    elif p�ev in range (1,29) and kuu==2 and not is_year_leap(aasta):
        v=True
    elif p�ev in range(1,31) and kuu in[4,6,9,11] and aasta>0:
        v=True
    else:
        v=True
    return v

