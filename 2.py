# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# 4 -> [1, 2, 6, 24]
# 6 -> [1, 2, 6, 24, 120, 720]

from math import factorial

n = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * factorial(x - 1)
list2 = list( f(i) for i in range(1, n +1))
print(list2)
