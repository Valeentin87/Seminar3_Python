# Напишите программу, которая найдёт произведение пар чисел списка. \
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
N = int(input('введите число элементов в списке N = '))
lst = [None]*N
for i in range(N):
    lst[i] = random.randint(0, 20)
print(lst)
multiplier = None
if len(lst)%2 == 0:
    multiplier = len(lst)/2
else:
    multiplier = len(lst)//2 + 1
lst_result = [None]*int(multiplier)
left_index = 0
right_index = len(lst) - 1
while left_index<=right_index:
    lst_result[left_index] = lst[left_index]*lst[right_index]
    left_index += 1
    right_index = right_index - 1
print(f' произведение сответствующих элементов списка {lst} равно {lst_result}')


