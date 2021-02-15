"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

#### 示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

#### 示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

#### 示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

提示：
1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4
"""


def max_profit(prices) -> int:
    peak, peak_i = -1, -1
    valley, valley_i = 0x7fffffff, -1

    prices_len = len(prices)
    profit = 0
    for i in range(prices_len):
        price = prices[i]
        if peak > price and peak_i == i - 1:
            if valley_i < peak_i:
                profit += (peak - valley)
            valley = 0x7fffffff
            valley_i = -1

        if valley < price and valley_i == i - 1:
            peak = -1
            peak_i = -1

        if peak <= price:
            peak = price
            peak_i = i

        if valley >= price:
            valley = price
            valley_i = i

    if peak_i > valley_i:
        profit += (peak - valley)
    return profit


def max_profit2(prices) -> int:
    length = len(prices)
    profit = 0
    for i in range(1, length):
        if prices[i] > prices[i - 1]:
            profit += (prices[i] - prices[i - 1])
    return profit


def max_profit3(prices) -> int:
    length, i = len(prices), 0
    profit = 0
    while i < length - 1:
        while i < length - 1 and prices[i] >= prices[i + 1]:
            i += 1
        vallay = prices[i]
        while i < length - 1 and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]

        profit += (peak - vallay)

    return profit


if __name__ == '__main__':
    print(max_profit([1, 2, 3, 4, 5]), max_profit2([1, 2, 3, 4, 5]), max_profit3([1, 2, 3, 4, 5]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]), max_profit2([7, 6, 5, 4, 3, 2, 1]), max_profit3([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([3, 4, 2, 7, 6, 5]), max_profit2([3, 4, 2, 7, 6, 5]), max_profit3([3, 4, 2, 7, 6, 5]))
    print(max_profit([7, 1, 5, 3, 6, 4]), max_profit2([7, 1, 5, 3, 6, 4]), max_profit3([7, 1, 5, 3, 6, 4]))
    print(max_profit([2, 1, 2, 1, 0, 0, 1]), max_profit2([2, 1, 2, 1, 0, 0, 1]), max_profit3([2, 1, 2, 1, 0, 0, 1]))
