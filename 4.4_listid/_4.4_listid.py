#  Работа со строками и списками 

tekst="Programmeerimine"
print(tekst) # просто выводим строку

tähed=list(tekst) # превращаем строку в список символов
print(tähed)

print(f"Viies täht on: {tähed[4]}") # выводим 5-й символ

print(f"Sõnas on kokku {len(tekst)} tähte") # считаем длину строки


#  Добавление элементов в список с помощью append() 

asjad=[] # создаем пустой список
for j in range(5):
asjad.append(input(f"Lisa {j+1}. element: ")) # добавляем элемент в список в конец
print(asjad) # выводим список

for a in asjad:
print(a) # выводим каждый элемент по одному


# Расширение списка extend() 

tähed.extend(asjad) # добавляем список asjad в список tähed
print(tähed)
print(asjad)


#  Добавление и удаление элементов 

asjad.insert(0,"Algus") # вставляем элемент в начало списка
print(asjad)

asjad.remove("Algus") # удаляем элемент "Algus"
print(asjad)

asjad.pop(0) # удаляем первый элемент
asjad.pop() # удаляем последний элемент
print(asjad)


# Поиск и подсчет 

pos=tähed.index("r") # ищем индекс первой буквы "r"
print(f"Täht 'r' on {pos}-positsioonil")

r_arv=tähed.count("r") # считаем количество букв "r"
print(f"Täht 'r' esineb {r_arv} korda")


#  Сортировка и копирование 

tähed.sort(reverse=True) # сортируем в обратном порядке
print(tähed)

tähed.reverse() # переворачиваем список
print(tähed)

tähed2=tähed.copy() # копируем список
tähed2.clear() # очищаем копию
print(tähed2)


#  Ülesanne 1 

from string import *

vokaalid=["a","e","i","o","u","õ","ä","ö","ü"]
konsonandid="bcdfghjklmnpqrstvwxyz"
numbrid=digits
märgid=punctuation

v=k=n=m=t=0

laused=input("Sisesta sõna või lause: ").lower() # переводим в нижний регистр
tähed=list(laused)

if " " in tähed:
print("See on lause")
for s in tähed:
if s in vokaalid:
v+=1
elif s in konsonandid:
k+=1
elif s in numbrid:
n+=1
elif s in märgid:
m+=1
elif s==" ":
t+=1
print(f"V: {v}\nK: {k}\nN: {n}\nM: {m}\nT: {t}")
else:
print(f"Kokku on {len(tähed)} märki")


#  Ülesanne 2.1 

nimed_list=[]
for i in range(5):
nimi=input("Sisesta nimi: ").lower()
nimed_list.append(nimi)
nimed_list.sort()
print("Nimekiri tähestikulises järjekorras:", nimed_list)
print("Viimati lisatud nimi:", nimi)
muuda=input("Millist nime soovid muuta?: ")
if muuda in nimed_list:
uus=input("Uus nimi: ")
ind=nimed_list.index(muuda)
nimed_list[ind]=uus
print("Uuendatud nimekiri:", sorted(nimed_list))
else:
print("Nime ei leitud.")


#  Ülesanne 2.2 

õpilased=['Juhan', 'Kati', 'Mario', 'Mati', 'Mati']
unikaalsed=[]
for nimi in õpilased:
if nimi not in unikaalsed:
unikaalsed.append(nimi)
print(unikaalsed)


#  Ülesanne 2.3

vanused=[5,13,25,9,20,17,11,10,8,24]
print(vanused)
print("Noorim:", min(vanused))
print("Vanim:", max(vanused))
print("Summa:", sum(vanused))
print("Keskmine:", sum(vanused)/len(vanused))


#  Ülesanne 7 
numbrid_list=[]
for i in range(5):
nr=int(input("Sisesta arv: "))
numbrid_list.append(nr)

suund=input("Kas sorteerida kasvavalt või kahanevalt? (kasv/kahan): ").lower()

if suund=="kasv":
numbrid_list.sort()
elif suund=="kahan":
numbrid_list.sort(reverse=True)
else:
print("Vale sisend. Sorteerime kasvavalt.")
numbrid_list.sort()

print("Sorteeritud arvud:", numbrid_list)


#  Ülesanne 3 

sisend=[10,15,30,45,60,25]
for num in sisend:
print("*" * num) # выводит столько * сколько указано в числе


#  Ülesanne 4 

piirkonnad={
"1":"Tallinn",
"2":"Narva, Narva-Jõesuu",
"3":"Kohtla-Järve",
"4":"Ida-Virumaa, Lääne-Virumaa, Jõgevamaa",
"5":"Tartu linn",
"6":"Tartumaa, Põlvamaa, Võrumaa, Valgamaa",
"7":"Viljandimaa, Järvamaa, Harjumaa, Raplamaa",
"8":"Pärnumaa",
"9":"Läänemaa, Hiiumaa, Saaremaa"
}

post=input("Sisesta postiindeks: ")

if post.isdigit() and len(post)==5:
reg=piirkonnad.get(post[0])
print(f"Piirkond: {reg}")
if post[0] in ["1","2","3"]:
print("Olge kodus!")
else:
print("Kandke maske!")
else:
print("Vigane sisend!")


#  Ülesanne 11

n=int(input("Mitu tähte soovid?: "))
tähed_list=[]
abc=list("abcdefghijklmnopqrstuvwxyz")

for i in range(n):
tähed_list.append(abc[i])

tähed_kordustega=[]
i=1
for täht in tähed_list:
tähed_kordustega.append(täht*i)
i+=1

print("Tähed:", tähed_list)
print("Kordustega:", tähed_kordustega)
