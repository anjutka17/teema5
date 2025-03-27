﻿# Импортируем все математические функции, например sqrt() и pi
from math import *

# Вывод текста
print("=== Ruudu omadused (Квадрат) ===")

# try - попытка выполнить блок кода. Если внутри произойдет ошибка, то перейдем к except
try:
# input() - ввод данных с клавиатуры
# int() - превращаем ввод в целое число
    a = int(input("Sisesta ruudu külje pikkus => "))

# if - условие. Проверяем, что введенное число больше нуля
    if a > 0:
# Вычисляем площадь квадрата S=a^2
        S = a ** 2
        print("Ruudu pindala (Площадь квадрата):", S)

# Вычисляем периметр квадрата P=4a
        P = 4 * a
        print("Ruudu ümbermõõt (Периметр квадрата):", P)

# Вычисляем диагональ квадрата через теорему Пифагора
        diag = a * sqrt(2)
        print("Ruudu diagonaal (Диагональ квадрата):", round(diag, 2)) # округляем до двух знаков
    else:
# else - альтернатива if, выполняется если условие не сработало (a <= 0)
     print("Külg ei saa olla 0 või väiksem!") # сторона не может быть <=0

# except - что делать, если внутри try случилась ошибка (например ввели не число)
except:
    print("Vigane sisestus! Palun sisesta täisarv.")# Введено не число


    


#Р А Б О Т А С П Р Я М О У Г О Л Ь Н И К О М 

print("\n=== Ristküliku omadused (Прямоугольник) ===")

try:

# Вводим обе стороны
    b = int(input("Sisesta esimese külje pikkus => "))
    c = int(input("Sisesta teise külje pikkus => "))

# and - логический оператор "и", проверяем два условия одновременно
    if b > 0 and c > 0:
        S = b * c # площадь прямоугольника
        print("Ristküliku pindala:", S)

        P = 2 * (b + c) # периметр прямоугольника
        print("Ristküliku ümbermõõt:", P)

        diag = sqrt(b**2 + c**2) # диагональ прямоугольника (по Пифагору)
        print("Ristküliku diagonaal:", round(diag, 2))
    else:
        print("Küljed peavad olema positiivsed!") # стороны должны быть больше 0

except:
    print("Vigane sisestus! Palun sisesta täisarvud.") # некорректный ввод


# Р А Б О Т А С К Р У Г О М 

    print("\n=== Ringi omadused (Круг) ===")

try:
# Вводим радиус
    r = float(input("Sisesta ringi raadius => ")) # можно вводить дробное число (float)

    if r > 0:
        d = 2 * r # диаметр круга
        print("Ringi läbimõõt:", d)

        S = pi * r ** 2 # площадь круга
        print("Ringi pindala:", round(S, 2))

        C = 2 * pi * r # длина окружности
        print("Ringjoone pikkus:", round(C, 2))
    else:
        print("Raadius peab olema suurem kui 0") # радиус должен быть больше 0

except:
    print("Vigane sisestus! Palun sisesta arv.") # ошибка при вводе
