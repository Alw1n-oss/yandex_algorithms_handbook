def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

n, k = map(int, input().split())

combination_with_repetition = factorial(n + k - 1) // (factorial(k) * factorial(n - 1))

print(combination_with_repetition)
