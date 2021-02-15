"""
零钱兑换 II

给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

示例 3:

输入: amount = 10, coins = [10]
输出: 1
 

注意:
你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数
"""
from typing import List


def change2(amount: int, coins: List[int]) -> int:
    options = []

    def solve(coins: List[int], rest: int, option: List[int]):
        if rest < 0:
            return
        elif rest == 0:
            opt = option.copy()
            opt.sort()
            if opt not in options:
                options.append(opt)
        else:
            n = len(coins)
            for i in range(n):
                option.append(coins[i])
                solve(coins, rest - coins[i], option)
                option.pop()

    solve(coins, amount, [])
    return len(options)

"""
1. 动态规划：题目求组合数，设dp[i][j]表示使用前i种***组成j金额的组合数。
2. 在(0,coins[i])，dp[i,j]=dp[i-1][j];在（coins[i],amount+1),dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]。
3. 状态转移方程 dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
4. 优化 
    dp[i][j-coins[i]]实际上是由dp[i-1][j]得来的，也就是说dp[i][j]只与dp[i-1]有关。故可降维为1维。
    因为dp[i][j-coins[i]]是由更新后的dp[i][j]的计算的，所以j使用正序
    dp[j] = dp[j] + dp[j-coins]
5. 时间复杂度：O(n * amount)，n为coins的种类数
6. 空间复杂度：O(amount)
"""


def change(amount: int, coins: List[int]) -> int:
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = dp[j] + dp[j - coin]
    return dp[amount]


if __name__ == '__main__':
    print(change(5, [1, 2, 5]))
    print(change(10, [1, 2, 5]))
    print(change(3, [2]))
    print(change(10, [10]))
    print(change(500, [1, 2, 5]))

