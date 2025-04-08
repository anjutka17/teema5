p=[]
i=[]
# �lesanne 1
def Lisa_andmed(p:list,i:list):
    """
    Lisab mitu inimesed ja nende palgad olemasolevatesse nimekirjadesse.
    :param inimesed: Inimeste nimede nimekiri
    :param palgad: Palgade nimekiri
    :param mitu: Kui palju inimesi lisada
    :rtype: None
    """
while True:
      try:
           nimi=input("Nimi: ")
           if nimi.isalpha():
               try:
                   palk=float(input("Palk: "))
               except:
                   print("palk on arv!")
               break
               print("Andmed on lisatud")
        
      except:
            print("Kirjuta ainult t�htede kasudates")
p.append(palk)
i.append(nimi)
 #�lesanne 2
def kustuta_andmed(p:list,i:list):
    """
   Kustutab nimekirjast sisestatud nime ja tema palga.
   :param inimesed: Inimeste nimede nimekiri
   :param palgad: Palgade nimekiri
   :param nimi: Kustutatava isiku nimi
   :rtype: None
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
                print("Andmed on kustutatud")
            else:
                 print("Andmed puuduvad!")
except:
      print("Kirjuta ainult t�htede kasudates")

#�lesanne 3
def suurim_palk(inimesed: list, palgad: list):
    """
Leiab suurima palga ja selle saaja nime.
:param inimesed: Inimeste nimede nimekiri
:param palgad: Palgade nimekiri
:rtype: tuple
   """
suurim = max(p)
print("Suurim palk on {suurim}")
k=p.count(suurim)
for j in range(k):
    ind = p.index(suurim, ind)
    print(f"Saab k�tte {i[ind]}")
    ind=ind+1
#�lesanne 4
def v�ikseim_palk(inimesed: list, palgad: list):
    """
Leiab v�iksem palga ja selle saaja nime.
:param inimesed: Inimeste nimede nimekiri
:param palgad: Palgade nimekiri
:rtype: None 
   """
v�ikseim = min(p)
print("V�ikseim palk on {v�ikseim}")
k=p.count(v�ikseim)
for j in range(k):
    ind = p.index(v�ikseim)
    print(f"Saab k�tte {i[ind]}")
    ind+=1

#�lesanne 5
def Sorteerimine_Kasvav(p:list,i:list) -> any:
    """
    Sorteerib palgad koos nimedega kasvavalt ja kahanevalt.
    :param inimesed: Inimeste nimekiri
    :param palgad: Palkade nimekiri
    :rtype: any
   """
while True:
    try:
       v=input("Vali m�rk: > (kasvav) v�i < (kahanev)")
       if v in(">","<"):
           break
       else:
           print("Ainult ">", "<" ")
    except:
        print("Viga! Proovi uuesti!")
        for n in range(0, len(i)):
           for m in range(n,len(i)):
             if eval(str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    

# �lesanne 6
    def V�rdsed_palgad(inimesed:list,palgad:list):
        """
    Leiab inimesed, kellel on v�rdne palk ja mitu neid on.
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype: None
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        if k>1:
            print(f"Palk{palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab k�tte {i[ind]}")
                ind+=1

# �lesanne 7
    def otsi_palk(i:list,p:list):
       """
    Otsib inimese nime j�rgi tema palga(d).
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype: None
    """
    nimi = input("Sisesta nimi: ").capitalize()
    print("Leitud palgad:")
    for j in range(len(i)):
        if i[j] == nimi:
            print(p[j])


# �lesanne 8

    def rohkem_vahem(i:list,p:list):
      """
    Kuvab inimesed, kes saavad rohkem v�i v�hem kui m��ratud summa.
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype: None
    """
    summa = int(input("Sisesta summa: "))
    valik = input("Kas soovid rohkem v�i v�hem? (r/v): ").lower()
    if valik == "r":
        for j in range(len(p)):
            if p[j] > summa:
                print(i[j], "-", p[j])
    elif valik == "v":
        for j in range(len(p)):
            if p[j] < summa:
                print(i[j], "-", p[j])
    else:
        print("Vale valik!")
