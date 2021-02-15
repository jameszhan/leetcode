"""
二进制求和

给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"


示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""


def add_binary(a: str, b: str) -> str:
    a_len, b_len = len(a), len(b)
    if a_len == 0 or a == '0':
        return b
    elif b_len == 0 or b == '0':
        return a

    if a_len < b_len:
        a = '0' * (b_len - a_len) + a
    if a_len > b_len:
        b = '0' * (a_len - b_len) + b

    i, j = len(a) - 1, len(b) - 1
    ans = ''
    carry = False
    while i >= 0 and j >= 0:
        need_carry = False
        if a[i] == '1' and b[j] == '1':
            val = '1' if carry else '0'
            need_carry = True
        elif a[i] == '1' or b[j] == '1':
            if carry:
                val = '0'
                need_carry = True
            else:
                val = '1'
        else:
            val = '1' if carry else '0'

        ans = val + ans
        carry = need_carry
        i -= 1
        j -= 1

    if carry:
        ans = '1' + ans

    return ans


if __name__ == '__main__':
    print(add_binary('1', '1'))
    print(add_binary('11', '11'))
    print(add_binary('11', '110'))



