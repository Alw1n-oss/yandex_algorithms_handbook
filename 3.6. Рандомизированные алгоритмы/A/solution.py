n = int(input())
a = list(map(int, input().split()))

pivot = a[0]
i = 1
for j in range(1, n):
    if a[j] < pivot:
        a[i], a[j] = a[j], a[i]
        i += 1

a[0], a[i - 1] = a[i - 1], a[0]

print(*a)
