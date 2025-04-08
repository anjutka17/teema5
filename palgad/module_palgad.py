p=[]
i=[]
def lisa_andmed(p:list,i:list):
    """Funktsioon leiab nende palgad ja mitu inimesed
    :param i: Sisend t�hed
    :param p: Sisend numbrid
    :rtype:M��remata t��p (str v�i float)
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
                print("Kirjuta ainult t�hed")
        except:
            print("Kirjuta ainult t�htede kasutades")
    p.append(palk)
    i.append(nimi)

def kustuta_andmed(p:list,i:list):
    """Funktsioon kustuta palgad ja inimesed,kui i ja p>0
    :param i: Sisend t�hed
    :param p: Sisend numbrid
    :param nimi: Sisend str
    :rtype:M��remata t��p (str v�i float)
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
            print("Kirjuta ainult t�htede kasutades")

def suurim_palk(p:list,i:list):
    """Funktsioon leiab suurim palgad inimestel
    :param i: Sisend t�hed
    :param p: Sisend numbrid
    :rtype:M��remata t��p (str v�i float)
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    ind=p.index(suurim)
    for j in range(k):
        ind=p.index(suurim,ind)
        print(f"Saab k�tte {i[ind]}")
        ind+=1

def v�iksem_palk(p:list,i:list):
    """Funktsioon leiab v�iksem palgad inimestel
    :param i: Sisend t�hed
    :param p: Sisend numbrid
    :rtype:M��remata t��p (str v�i float)
    """
    v�iksem=max(p)
    print(f"V�iksem palk on {v�iksem}")
    k=p.count(v�iksem)
    ind=p.index(v�iksem)
    for j in range(k):
        ind=p.index(v�iksem,ind)
        print(f"Saab k�tte {i[ind]}")
        ind+=1

def kas_kah_palk(p:list,i:list)->any:
    """Funktsioon j�rjesab palgad kasvavas ja kahanevas j�rjekorras koos nimedega
    :param inimesed: Inimeste nimekiri
    :param palgad: Palkade nimekiri
    :rtype: any
    """
    while True:
        try:
            v=input("Vali m�rk: >(kasvav) v�i < (kahanev)")
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

       

def v�rdsed_palk(p:list,i:list):
    """Funktsioon leiab kes saavad v�rdset palka, ja kui palju neid on ja kuvada nende andmed ekraanile
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
                print(f"Saab k�tte {i[ind]}")
                ind+=1


