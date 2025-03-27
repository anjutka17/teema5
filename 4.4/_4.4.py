# Работа со строками и списками

tekst = "Programmeerimine" # обычная строка (тип данных str)
print(tekst) # просто выводим строку

tähed = list(tekst) # list() - превращаем строку в список символов
print(tähed)

print(f"Viies täht on: {tähed[4]}") # [4] - обращаемся к 5-му символу (нумерация с нуля)

print(f"Sõnas on kokku {len(tekst)} tähte") # len() - считает количество символов в строке


#Добавление элементов в список с помощью append()
asjad = [] # создаем пустой список
for j in range(5): # range(5) - цикл от 0 до 4 (всего 5 раз)
asjad.append(input(f"Lisa {j+1}. element: ")) # input() - ввод текста, append() - добавляем в конец списка
print(asjad)

for a in asjad: # перебираем список и выводим каждый элемент
print(a)


#Расширение списка extend()

tähed.extend(asjad) # extend() - добавляем все элементы другого списка в конец текущего
print(tähed)
print(asjad)


# Добавление и удаление элементов

asjad.insert(0, "Algus") # insert(позиция, элемент) - вставляем элемент в указанную позицию
print(asjad)

asjad.remove("Algus") # remove() - удаляет элемент по значению
print(asjad)

asjad.pop(0) # pop() - удаляет элемент по индексу, здесь удаляем первый
asjad.pop() # без аргументов pop() удаляет последний элемент
print(asjad)


# Поиск и подсчет

pos = tähed.index("r") # index() - возвращает индекс первого найденного элемента
print(f"Täht 'r' on {pos}-positsioonil")

r_arv = tähed.count("r") # count() - считает, сколько раз встречается элемент
print(f"Täht 'r' esineb {r_arv} korda")


# Сортировка и копирование

tähed.sort(reverse=True) # sort() - сортирует список, reverse=True - в обратном порядке
print(tähed)

tähed.reverse() # reverse() - переворачивает список
print(tähed)

tähed2 = tähed.copy() # copy() - создает копию списка
tähed2.clear() # clear() - очищает список
print(tähed2)


#Ülesanne 1

from string import * # импортируем готовые строки с буквами, цифрами и символами

vokaalid = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"] # список гласных
konsonandid = "bcdfghjklmnpqrstvwxyz" # строка согласных
numbrid = digits # готовая строка из модуля string: '0123456789'
märgid = punctuation # готовая строка с символами: '!"#$%&...'

# v, k, n, m, t - счетчики
v = k = n = m = t = 0

laused = input("Sisesta sõna või lause: ").lower() # .lower() - приводит строку к нижнему регистру
tähed = list(laused) # превращаем строку в список символов

if " " in tähed: # проверяем есть ли пробел - значит это фраза
print("See on lause")
for s in tähed:
if s in vokaalid:
v += 1
elif s in konsonandid:
k += 1
elif s in numbrid:
n += 1
elif s in märgid:
m += 1
elif s == " ":
t += 1
print(f"V: {v}\nK: {k}\nN: {n}\nM: {m}\nT: {t}")
else:
print(f"Kokku on {len(tähed)} märki") # считаем символы


# Ülesanne 2.1

nimed_list = [] # пустой список
for i in range(5):
nimi = input("Sisesta nimi: ").lower() # приводим к нижнему регистру
nimed_list.append(nimi)
nimed_list.sort() # сортируем по алфавиту
print("Nimekiri tähestikulises järjekorras:", nimed_list)
print("Viimati lisatud nimi:", nimi)

muuda = input("Millist nime soovid muuta?: ")
if muuda in nimed_list: # проверяем есть ли имя в списке
uus = input("Uus nimi: ")
ind = nimed_list.index(muuda) # находим индекс старого имени
nimed_list[ind] = uus # заменяем
print("Uuendatud nimekiri:", sorted(nimed_list))
else:
print("Nime ei leitud.")


# Ülesanne 2.2

õpilased = ['Juhan', 'Kati', 'Mario', 'Mati', 'Mati']
unikaalsed = [] # для уникальных имен
for nimi in õpilased:
if nimi not in unikaalsed: # если имя еще не добавлено
unikaalsed.append(nimi)
print(unikaalsed)


#Ülesanne 2.3

vanused = [5, 13, 25, 9, 20, 17, 11, 10, 8, 24]
print(vanused)
print("Noorim:", min(vanused)) # min() - наименьший
print("Vanim:", max(vanused)) # max() - наибольший
print("Summa:", sum(vanused)) # sum() - сумма всех чисел
print("Keskmine:", sum(vanused) / len(vanused)) # среднее значение


#Ülesanne 7

numbrid_list = [] # список для чисел
for i in range(5):
nr = int(input("Sisesta arv: ")) # int() - превращаем ввод в число
numbrid_list.append(nr)

suund = input("Kas sorteerida kasvavalt või kahanevalt? (kasv/kahan): ").lower()

if suund == "kasv":
numbrid_list.sort()
elif suund == "kahan":
numbrid_list.sort(reverse=True)
else:
print("Vale sisend. Sorteerime kasvavalt.")
numbrid_list.sort()

print("Sorteeritud arvud:", numbrid_list)


# Ülesanne 3 

sisend = [10, 15, 30, 45, 60, 25]
for num in sisend:
print("*" * num) # выводит строку из "*" длиной num


# Ülesanne 4
piirkonnad = {
"1": "Tallinn",
"2": "Narva, Narva-Jõesuu",
"3": "Kohtla-Järve",
"4": "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa",
"5": "Tartu linn",
"6": "Tartumaa, Põlvamaa, Võrumaa, Valgamaa",
"7": "Viljandimaa, Järvamaa, Harjumaa, Raplamaa",
"8": "Pärnumaa",
"9": "Läänemaa, Hiiumaa, Saaremaa"
}

post = input("Sisesta postiindeks: ")

if post.isdigit() and len(post) == 5: # isdigit() - проверка, что строка состоит только из цифр
 reg = piirkonnad.get(post[0]) # get() - получить значение по ключу
print(f"Piirkond: {reg}")
if post[0] in ["1", "2", "3"]:
  print("Olge kodus!") # если зона повышенного риска
else:
  print("Kandke maske!")
else:
print("Vigane sisend!")


# Ülesanne 11

n = int(input("Mitu tähte soovid?: "))
tähed_list = []

abc = list("abcdefghijklmnopqrstuvwxyz") # создаем список из латинского алфавита

for i in range(n):
tähed_list.append(abc[i]) # добавляем первые n букв

tähed_kordustega = [] # список с буквами, повторенными i раз
i = 1
for täht in tähed_list:
tähed_kordustega.append(täht * i)
i += 1

print("Tähed:", tähed_list)
print("Kordustega:", tähed_kordustega)