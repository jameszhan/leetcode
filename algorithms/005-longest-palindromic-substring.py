"""
最长回文子串

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。


示例 2：

输入: "cbbd"
输出: "bb"
"""


def longest_palindrome(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    else:
        start, end, max_len = 0, 0, 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        start = j
                        end = i
        return s[start:end+1]


if __name__ == '__main__':
    print(longest_palindrome('babad'))
    print(longest_palindrome('cbbd'))