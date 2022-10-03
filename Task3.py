# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным \
# и минимальным значением дробной части элементов.
import random
N = int(input('введите число элементов в списке N = '))
lst = [None]*N
for i in range(N):
    lst[i] = round(random.uniform(0.01, 20), 2)
print(lst)
max_fractional = lst[1]*100%100/100
min_fractional = lst[i]*100%100/100
for i in range(len(lst)):
    if lst[i]*100%100/100>max_fractional:
        max_fractional = lst[i]*100%100/100
    if lst[i]*100%100/100<min_fractional:
        min_fractional = lst[i]*100%100/100
answer = max_fractional - min_fractional
print(f'разница между максимальной и минимальной дробной частью в последовательности равна {answer}')



