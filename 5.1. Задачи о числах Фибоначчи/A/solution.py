listF = {}

def fibonacci(n):
    global listF
    l = len(listF)
    if l <= n:
        for i in range(n - l + 1):
            listF.append(None)
    if listF[n] == None:
        if n <= 1:
            listF[n] = n
        else:
            listF[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return listF[n]

if __name__ == "__main__":
    n = int(input())
    
    listF = [0, 1]
    print(fibonacci(n))
