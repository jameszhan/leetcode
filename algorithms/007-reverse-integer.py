
"""
出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

#### 示例 1:

输入: 123
输出: 321

#### 示例 2:

输入: -123
输出: -321

#### 示例 3:

输入: 120
输出: 21

> 注意: 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31−1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


def reverse(n: int) -> int:
    v = 0
    f = 1 if n > 0 else -1
    n = n * f
    while True:
        v = v * 10 + n % 10
        n = n // 10
        if n == 0 or n == -1:
            break
    v = v * f
    if v > 0x7fffffff or v < -0x80000000:
        return 0
    else:
        return v


if __name__ == '__main__':
    print(reverse(321))
    print(reverse(-312))
    print(reverse(120))
    print(reverse(1534236469))
    print(reverse(1563847412))
