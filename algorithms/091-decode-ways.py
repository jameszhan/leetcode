"""
解码方法

一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。


示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
"""


def num_decodings(s: str) -> int:
    s_len = len(s)
    if s_len <= 0:
        return 0
    elif s_len == 1:
        return 0 if s == '0' else 1
    else:
        # 傻逼测试用例
        if s[0] == '0':
            return 0

        # dp[i]：以 s[i] 结尾的前缀字符串的解码个数
        # 分类讨论：
        # 1、s[i] != '0' 时，dp[i] = dp[i - 1]
        # 2、10 <= s[i - 1..i] <= 26 时，dp[i] += dp[i - 2]
        dp = [0 for _ in range(s_len)]
        dp[0] = 1
        for i in range(1, s_len):
            if s[i] != '0':
                dp[i] = dp[i - 1]

            val = int(s[i-1:i+1])

            if 10 <= val <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]

        return dp[s_len - 1]


if __name__ == '__main__':
    print(num_decodings('01'))
    print(num_decodings('12'))
    print(num_decodings('226'))

