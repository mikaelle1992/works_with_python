

def fatorial(n):
    return n * (fatorial(n - 1) if (n-1) > 1 else 1)
    # 10! = 10 . 9 . 8 . 7 . 6 . 5 . 4 . 3 . 2 . 1 = 3.628.800


print(f'10! = {fatorial(10)}')