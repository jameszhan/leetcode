"""
验证回文串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:

输入: "race a car"
输出: false
"""


def is_palindrome(s: str) -> bool:
    def is_valid_char(ch):
        if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9':
            return True
        else:
            return False

    s_len = len(s)
    if s_len <= 1:
        return True
    else:
        i, j = 0, s_len - 1
        while i < j:
            si, sj = s[i], s[j]
            if not is_valid_char(si):
                i += 1
                continue
            if not is_valid_char(sj):
                j -= 1
                continue

            if si == sj:
                i += 1
                j -= 1
            elif si.lower() == sj.lower():
                i += 1
                j -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    print(is_palindrome("0P"))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))
    print(is_palindrome("race a e car"))