# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input('введите число в десятичной системе исчисления'))
remains = 0
whole = 0
binary = ' '
while number//2 !=0 and number//2 != 1:
    remain = number%2
    binary = binary + str(remain)
    number = number//2
print(binary)