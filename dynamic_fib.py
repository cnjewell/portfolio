def accum_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibA = 0
        fibB = 1
        for num in range(1, n):
            fibC = fibA + fibB
            fibA = fibB
            fibB = fibC
        return fibB

def recursive_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fib(n-2) + recursive_fib(n-1)

def dynamic_fib(n):
    fibs = {0:0, 1:1}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in fibs:
        return fibs[n]
    else:
        for num in range(2, n+1):
            newfib = fibs[num-2] + fibs[num-1]
            fibs[num] = newfib
        return fibs[n]

def main():
    pass

if __name__ == "__main__":
    main()


