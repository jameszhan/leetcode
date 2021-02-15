"""
最佳买卖股票时机含冷冻期

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

#### 示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""


def max_profit(prices) -> int:
    days = len(prices)
    if days <= 1:
        return 0

    hold, sold, frozen = -0x80000000, 0, 0
    for i in range(days):
        price = prices[i]
        pre_sold = sold
        hold = max(hold, frozen + -price)
        sold = max(sold, hold + price)
        if i > 0:
            frozen = max(frozen, pre_sold)

    return sold


if __name__ == '__main__':
    print(max_profit([1, 2, 3, 0, 2]))


"""
dp0[i]: 第i天结束，手头没有股票时的最大利润
dp1[i]: 第i天结束，手头有股票时的最大利润
cool[i]: 第i天结束且第i天处于冷冻期时的最大利润

dp0[i] = max(dp0[i-1], dp1[i-1] + prices[i]); // 保持 or 卖出
dp1[i] = max(dp1[i-1], cool[i-1] - prices[i]); // 保持 or (冷却 -> 买入)
cool[i] = max(cool[i-1], dp0[i-1]); // 第i-1天结束时没有股票说明第i天可以是冷却期
"""