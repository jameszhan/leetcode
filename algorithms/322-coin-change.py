"""
零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:

输入: coins = [2], amount = 3
输出: -1
"""
from typing import List


def coin_change2(coins: List[int], amount: int) -> int:
    ans = 0x7FFFFFFF

    def solve(coins: List[int], amount: int, count: int):
        nonlocal ans
        if amount < 0:
            return
        elif amount == 0:
            ans = min(ans, count)
        else:
            for i in range(len(coins)):
                solve(coins, amount - coins[i], count + 1)

    n = len(coins)
    if n == 0:
        return 1 if amount == 0 else 0
    elif n == 1:
        return 1 if coins[0] == amount else -1
    else:
        solve(coins, amount, 0)
        return ans


def coin_change(coins: List[int], amount: int) -> int:
    memo = {}

    def solve(coins: List[int], amount: int):
        # print(coins, amount)
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        else:
            if amount in memo:
                return memo[amount]

            min = 0x7FFFFFF
            for i in range(len(coins)):
                res = solve(coins, amount - coins[i])
                if res >= 0 and res < min:
                    min = res + 1           # 加上减于coins[i]这次

            memo[amount] = -1 if min == 0x7FFFFFF else min
            return memo[amount]

    n = len(coins)
    if amount == 0:
        return 0
    elif n == 0:
        return 1 if amount == 0 else 0
    else:
        return solve(coins, amount)


if __name__ == '__main__':
    print(coin_change([1, 2, 5], 11))
    print(coin_change([1, 2, 5], 15))
    print(coin_change([1, 2, 5], 13))
    print(coin_change([1, 5], 13))
    print(coin_change([1, 2, 5], 30))
    print(coin_change([2], 3))
    print(coin_change([1], 0))
    print(coin_change([1], 2))

