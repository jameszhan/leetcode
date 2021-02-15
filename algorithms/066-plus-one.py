"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。


示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""


def plus_one(digits):
    length = len(digits)
    if length <= 0:
        return []

    ans = []
    carry = True
    for i in reversed(range(length)):
        digit = digits[i]

        if carry:
            if digit == 9:
                ans.append(0)
                carry = True
            else:
                ans.append(digit + 1)
                carry = False
        else:
            ans.append(digit)

    if carry:
        ans.append(1)
    return list(reversed(ans))


if __name__ == '__main__':
    print(plus_one([1, 2, 3]))
    print(plus_one([4, 3, 2, 1]))
    print(plus_one([9, 9, 9]))
    print(plus_one([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
