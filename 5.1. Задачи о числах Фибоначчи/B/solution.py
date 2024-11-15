def last_digit_fibonacci(n):
    if n <= 1:
        return n


    fib_last_digits = [0, 1]

    
    for i in range(2, n + 1):
        fib_last_digits.append((fib_last_digits[i - 1] + fib_last_digits[i - 2]) % 10)

    
    return fib_last_digits[n] 


n = int(input())


print(last_digit_fibonacci(n))

            
