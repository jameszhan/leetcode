"""
两数相除

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2

提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
"""


def divide(dividend: int, divisor: int) -> int:
    sign = (dividend > 0) ^ (divisor > 0)
    if dividend == 0:
        return 0
    elif divisor == 1:
        return dividend
    elif divisor == -1:
        if dividend > -0x80000000:
            return -dividend
        else:
            return 0x7FFFFFFF
    if divisor == 1 or divisor == -1:
        return dividend if divisor == 1 else -dividend

    divisor = abs(divisor)
    dividend = abs(dividend)
    total = divisor
    count = 0
    while dividend >= total:
        count += 1
        total <<= 1

    ans = 0
    while count > 0:
        count -= 1
        total >>= 1
        if total <= dividend:
            ans += 1 << count
            dividend -= total

    # while total <= dividend:  # 超时
    #     total += divisor
    #     ans += 1
    return ans * -1 if sign else ans


if __name__ == '__main__':
    print(divide(10, 3))
    print(divide(7, -3))
    print(divide(8, 2))
    print(divide(1024, 2))
    print(divide(-2147483648, -1))
    print(divide(2147483647, 2))