n, k = map(int, input().split())

def factorial(x):
  if x == 0:
    return 1
  else:
    result = 1
    for i in range(1, x+1):
      result *= i
    return result

result = factorial(n) // (factorial(k) * factorial(n-k))
print(result)
