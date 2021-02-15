"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

#### 示例 1:

输入: 1
输出: true
解释: 2^0 = 1


#### 示例 2:

输入: 16
输出: true
解释: 2^4 = 16


#### 示例 3:

输入: 218
输出: false
"""


def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    return n & (n - 1) == 0


if __name__ == '__main__':
    print(is_power_of_two(0))
    print(is_power_of_two(1))
    print(is_power_of_two(16))
    print(is_power_of_two(218))