"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

#### 示例 1:

输入: 4
输出: 2

#### 示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
"""


def my_sqrt(n: int) -> int:
    def derivative(g, dx):
        return lambda x: (g(x + dx) - g(x)) / dx

    def solve(g, initial, epsilon):
        guess, i = initial, 0
        while abs(g(guess)) > epsilon:
            print('[ Epoch {0} ] guess = {1}'.format(i, guess))
            guess -= (g(guess) / (derivative(g, epsilon)(guess)))
            i += 1
        return guess

    return int(solve(lambda x: x ** 2 - n, n, 1e-6))


if __name__ == '__main__':
    print(my_sqrt(4))
    print(my_sqrt(8))
    print(my_sqrt(36))

