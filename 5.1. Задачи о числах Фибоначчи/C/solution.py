def matrix_multiply(A, B, m):

    C = [[0, 0], [0, 0]]
    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % m
    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % m
    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % m
    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % m
    return C

def fast_matrix_exponentiation(D, n, m):
    
    if n == 0:
        return [[1, 0], [0, 1]]  # Единичная матрица
    elif n % 2 == 0:  # Чётное n
        Y = fast_matrix_exponentiation(D, n // 2, m)
        return matrix_multiply(Y, Y, m)
    else:  # Нечётное n
        Y = fast_matrix_exponentiation(D, (n - 1) // 2, m)
        Y2 = matrix_multiply(Y, Y, m)
        return matrix_multiply(Y2, D, m)

def fibonacci_modulo_m(n, m):
 
    if n <= 1:
        return n
    M = [[0, 1], [1, 1]]
    P = fast_matrix_exponentiation(M, n, m)
    return P[0][1]

n, m = map(int, input().split())
print(fibonacci_modulo_m(n, m))
