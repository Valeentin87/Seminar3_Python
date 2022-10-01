# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,\
# стоящих на нечётной позиции.
import random
N = int(input('введите количество элементов списка '))
summa = 0
lst = [None]*N
string_out = ''
for i in range(N):
    lst[i] = random.randint(0 , 10)
print(lst)
for i in range(1, N, 2):
    summa = summa + lst[i]
    string_out = string_out + ',' + str(i)
print(f'сумма нечетных элементов {string_out} последовательности равна {summa}')

