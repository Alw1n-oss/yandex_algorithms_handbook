n = int(input())

sequences = []
for _ in range(n):
    m = int(input())
    sequence = list(map(int, input().split()))
    sequences.append(sequence)

merged_sequence = []
for i in range(n):
    merged_sequence += sequences[i]

merged_sequence.sort()
print(*merged_sequence)
