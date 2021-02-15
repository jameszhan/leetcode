import math
import time


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    dp = {}

    def solve(m):
        if m == 0 or m == 1:
            return m
        if m - 1 not in dp:
            dp[m - 1] = solve(m - 1)
        if m - 2 not in dp:
            dp[m - 2] = solve(m - 2)
        return dp[m - 1] + dp[m - 2]

    return solve(n)


def fibonacci2(n):
    if n < 2:
        return n
    else:
        x, y = 1, 0
        for i in range(2, n + 1):
            x, y = y, x
            x = x + y
        return x


def fibonacci3(n):
    sqrt5 = math.sqrt(5)
    c1, c2 = (1 + sqrt5) / 2, (1 - sqrt5) / 2
    return math.floor((math.pow(c1, n) - math.pow(c2, n)) / sqrt5)


if __name__ == '__main__':
    start = time.time()
    for i in range(50):
        print(fibonacci2(i))
    end = time.time()

    time1 = end - start

    start = time.time()
    for i in range(50):
        print(fibonacci3(i))
    end = time.time()

    time2 = end - start

    start = time.time()
    for i in range(50):
        print(fibonacci(i))
    end = time.time()

    time3 = end - start

    print("time1 = ", time1)
    print("time2 = ", time2)
    print("time3 = ", time3)

