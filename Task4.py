# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input('введите число в десятичной системе исчисления'))
remains = 0
whole = 0
binary = ''
while number // 2 != 0:
    remains = number % 2
    binary = binary + str(remains)
    number = number // 2

result_binary = str(number)
j = 0
for i in range(len(binary)):
    result_binary = result_binary + binary[j-1]
    j = j-1
print(f'результат в двоичной системе исчисления равен {result_binary}')
