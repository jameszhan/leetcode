"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

#### 示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

#### 示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7

#### 解释:

在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
"""


def max_profit(k: int, prices) -> int:
    days = len(prices)
    if days <= 1 or k == 0:
        return 0

    if k < days:
        holds = [-0x80000000 for _ in range(k)]
        solds = [0 for _ in range(k)]
        for i in range(days):
            price = prices[i]

            for j in range(k):
                if j == 0:
                    holds[j] = max(holds[j], -price)
                else:
                    holds[j] = max(holds[j], solds[j - 1] + -price)
                solds[j] = max(solds[j], holds[j] + price)
        return solds[-1]
    else:
        hold, sold = -0x80000000, 0
        for i in range(days):
            price = prices[i]
            hold = max(hold, sold + -price)
            sold = max(sold, hold + price)
        return sold


if __name__ == '__main__':
    print(max_profit(0, [1, 3]))
    print(max_profit(2, [2, 4, 1]))
    print(max_profit(2, [3, 2, 6, 5, 0, 3]))
