# Ülesanne 9: Pisike korrutustabel

# Генерируем таблицу умножения на 5 с помощью цикла for
for i in range(1, 11): # Перебираем числа от 1 до 10
  print(f"5 x {i} = {5 * i}") # Выводим результат умножения

# Ülesanne 8: Paaris ja paaritu

# Счётчики для чётных и нечётных чисел
paaris = 0 # Чётные числа
paaritu = 0 # Нечётные числа
# Генерируем числа от 1 до 100 с проверкой на чётность
for i in range(1, 101):
    if i % 2 == 0: # Проверяем, является ли число чётным
      print(f"{i} on paaris") # Выводим сообщение о чётном числе
      paaris += 1 # Увеличиваем счётчик чётных чисел
else:
  print(f"{i} on paaritu") # Выводим сообщение о нечётном числе
paaritu += 1 # Увеличиваем счётчик нечётных чисел

print(f"Kokku paaris: {paaris}, paaritu: {paaritu}") # Выводим общее количество

# Ülesanne 6: Tärnid
# 5x5 звёзд
print("5x5 tärnid: ")
for _ in range(5):
 print('*' * 5) # Печатаем 5 звёзд подряд
# Растущий треугольник звёзд
print("Kasvav kolmnurk: ")
for i in range(1, 6):
 print('*' * i) # Печатаем количество звёзд, равное номеру строки
# Убывающий треугольник звёзд
print("Kahanev kolmnurk: ")
for i in range(5, 0, -1):
 print('*' * i) # Печатаем количество звёзд, равное номеру строки

# Ülesanne 7: Loto
# Импортируем модуль random
# Модуль random предоставляет функции для работы со случайными числами,
# включая генерацию случайных целых чисел и чисел с плавающей точкой
import random

print("Loto numbrid: ")
loto_number = ''.join(str(random.randint(0, 9)) for _ in range(5)) # Генерируем 5 случайных цифр
print(loto_number) # Выводим сгенерированные цифры

# Ülesanne 16: Mis arv mõtles välja arvuti?

# Компьютер загадывает случайное число
number = random.randint(1, 100) # Генерируем случайное число от 1 до 100
print("Arvuti mõtles välja arvu vahemikus 1 kuni 100.")

while True:
    user_input = input("Arva ära arv (või kirjuta "lõpp" lõpetamiseks): ") # Получаем ввод пользователя
    if user_input.lower() == "lõpp": # Проверяем, хочет ли пользователь завершить игру
      print("Mäng lõppes!")
      break
    try:
       guess = int(user_input) # Пытаемся преобразовать ввод в число
       if guess == number:
           print("Õige! Sa arvasid arvu ära!")
           break
       elif guess < number:
           print("Arv on suurem.") # Подсказка: загаданное число больше
       else:
           print("Arv on väiksem.") # Подсказка: загаданное число меньше
    except ValueError:
        print('Palun sisesta korrektne number või "lõpp".') # Обработка ошибки ввода
