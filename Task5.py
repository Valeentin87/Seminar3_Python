# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
N = int(input('введите число N = '))
fib1 = fib2 = 1
print(fib1, fib2, end=' ')
for i in range(-N, N):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')