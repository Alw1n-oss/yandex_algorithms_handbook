n = int(input())

# Факториал числа
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

# Вычисляем число перестановок
permutation = factorial(n)

print(permutation)
