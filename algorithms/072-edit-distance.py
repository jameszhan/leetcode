"""
编辑距离

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')


示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""

"""
# 初始化 dp，以 'horse' 和 'ros' 为例，此时的 dp 为：
#   0   1   2   3
#   1   0   0   0
#   2   0   0   0
#   3   0   0   0
#   4   0   0   0
#   5   0   0   0
"""


def min_distance(word1: str, word2: str) -> int:
    w1_len, w2_len = len(word1), len(word2)
    if w1_len == 0:
        return w2_len
    elif w2_len == 0:
        return w1_len
    else:
        dp = [[0 for _ in range(w2_len + 1)] for _ in range(w1_len + 1)]

        # 边界状态初始化
        for i in range(w1_len + 1):
            dp[i][0] = i
        for j in range(w2_len + 1):
            dp[0][j] = j

        # 计算所有 DP 值
        for i in range(1, w1_len + 1):
            for j in range(1, w2_len + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[w1_len][w2_len]


if __name__ == '__main__':
    print(min_distance("horse", "ros"))
    print(min_distance("intention", "execution"))