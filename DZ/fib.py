def Get_Fib_n(n: int):
    prev, cur = 0, 1
    for i in range(n):
        yield cur
        prev, cur = cur, prev+cur

if __name__ == '__main__':
    print(*Get_Fib_n(6))