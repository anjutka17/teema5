
from module_palgad import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Andmed")
    print(inimesed)
    print(palgad)
    print("Vajuta:\n1-Andmete lisamiseks\n2-Andmete kustutamiseks nime j�rgi\n3-Suurima palga leidmiseks\n4-V�iksem palga leidmiseks\n5-Sorteerimine j�rjend leidmiseks\n6-V�rdsed palgad leidmiseks ")
    v=int(input())
    if v==1:
        k=int(input("Mitu inimest?: "))
        for i in range(k):
            Lisa_andmed(palgad,inimesed)
    elif v==2:
        kustuta_andmed(palgad,inimesed)
    elif v==3:
        suurim_palk(palgad,inimesed)
    elif v==4:
        v�ikseim_palk(palgad,inimesed)
    elif v==5:
        palgad,inimesed=Sorteerimine_Kasvav(palgad,inimesed)
    elif v==6:
        V�rdsed_palgad(palgad,inimesed)
    elif v==7:
        otsi_palk(palgad,inimesed)
    elif v==8:
        rohkem_vahem(palgad, inimesed)