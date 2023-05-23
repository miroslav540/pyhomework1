import os
clear = lambda: os.system('cls')

# Task 1


print(' Task 1 ')
a = int(input('Введите длину стороны "a" ==> '));
b = int(input('Введите длину стороны "b" ==> '));
c = int(input('Введите длину стороны "c" ==> '));

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Треугольник не существует')
else:
    print('Треугольник существует')
    if a == b or a == c or b == c:
        print('Треугольник равнобедреный')
    if a == b and a == c:
        print('Треугольник равносторонний')

#  Task 2

print(' Task 2 ')

a = -1
while a < 0 or a > 100000:
    try: a = int(input('Введите a от 1 до 100000 => '))
    except: print('Введите число')

print(f'Введено {a}')
step = 2
flag = 'простое'
while step < a:
    if (a % step) == 0:
        flag = 'составное'
        break
    else: step += 1
print(f'число {a} - {flag}')


print('Task 3 ')
from random import randint

def input_data():
    a = -1
    while a < 0 or a > 1000:
        try: a = int(input('Введите a от 0 до 1000 => '))
        except: print('Введите число')
    return a

d = randint(0,1000)
flag = 'проиграл'
step = 10
print(f'Число от 0 до 1000 загадано. Ходите\n')
while step != 0 :
    a = int(input('Введите a от 0 до 1000 => '))
    if a > d:
        print(f'Меньше')
        step -= 1
    elif a < d:
        print(f'Больше')
        step -= 1
    elif a == d:
        flag = 'угадал'
        break
if step == 0:
    print(f'Ходы закончились ты {flag}')
else: print(f'ты {flag}')