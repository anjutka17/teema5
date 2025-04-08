p=[]
i=[]
def lisa_andmed(p:list,i:list):
    """Funktsioon leiab nende palgad ja mitu inimesed
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :rtype:Määremata tüüp (str või float)
    """
    while True:
        try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                try:
                    palk=float(input("Palk: "))
                except:
                    print("Palk on arv")
                break
                print("Andmed on lisatud")
            else:
                print("Kirjuta ainult tähed")
        except:
            print("Kirjuta ainult tähtede kasutades")
    p.append(palk)
    i.append(nimi)

def kustuta_andmed(p:list,i:list):
    """Funktsioon kustuta palgad ja inimesed,kui i ja p>0
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :param nimi: Sisend str
    :rtype:Määremata tüüp (str või float)
    """
    try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                k=i.count(nimi)
                if k>0:
                    for j in range(k):
                        ind=i.index(nimi)
                        i.pop(ind)
                        p.pop(ind)
                        print("Andmed on lisatud")
            else:
                print("Andmed puuduvad!")
    except:
            print("Kirjuta ainult tähtede kasutades")

def suurim_palk(p:list,i:list):
    """Funktsioon leiab suurim palgad inimestel
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :rtype:Määremata tüüp (str või float)
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    ind=p.index(suurim)
    for j in range(k):
        ind=p.index(suurim,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1

def väiksem_palk(p:list,i:list):
    """Funktsioon leiab väiksem palgad inimestel
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :rtype:Määremata tüüp (str või float)
    """
    väiksem=max(p)
    print(f"Väiksem palk on {väiksem}")
    k=p.count(väiksem)
    ind=p.index(väiksem)
    for j in range(k):
        ind=p.index(väiksem,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1

def kas_kah_palk(p:list,i:list)->any:
    """Funktsioon järjesab palgad kasvavas ja kahanevas järjekorras koos nimedega
    :param inimesed: Inimeste nimekiri
    :param palgad: Palkade nimekiri
    :rtype: any
    """
    while True:
        try:
            v=input("Vali märk: >(kasvav) või < (kahanev)")
            if v in('>','<'):
                break
            else:
                print("Ainult "<" ja ">"")
        except:
            print("Viga! Proovi uuesti!")
            for n in range(0,len(i)):
                for m in range(n,len(i)):
                    if eval(str(p[n])+v+str+(p[m])):
                        p[n],p[m]=p[m],p[n]
                        i[n],i[m]=i[m],i[n]

       

def võrdsed_palk(p:list,i:list):
    """Funktsioon leiab kes saavad võrdset palka, ja kui palju neid on ja kuvada nende andmed ekraanile
    :param inimesed: Inimeste nimekiri
    :param palgad: Palkade nimekiri
    :rtype:none
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1


