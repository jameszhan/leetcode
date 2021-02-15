"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


#### 示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。


#### 示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。


#### 示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
"""


# def max_profit(prices) -> int:
#     prices_len = len(prices)
#
#     peaks, valleys = [], []
#     peak, peak_i = -1, -1
#     valley, valley_i = 0x7fffffff, -1
#     for i in range(prices_len):
#         price = prices[i]
#         if peak > price and peak_i == i - 1:
#             peaks.append((peak_i, peak))
#             valley = 0x7fffffff
#             valley_i = -1
#
#         if valley < price and valley_i == i - 1:
#             valleys.append((valley_i, valley))
#             peak = 0
#             peak_i = -1
#
#         if peak < price:
#             peak = price
#             peak_i = i
#
#         if valley > price:
#             valley = price
#             valley_i = i
#
#     # print((current_peak, current_peak_i), (current_valley, current_valley_i))
#     if valley_i < peak_i:
#         peaks.append((prices_len - 1, prices[prices_len - 1]))
#
#     print('peaks: ', peaks)
#     print('valleys', valleys)


def max_profit(prices) -> int:
    days = len(prices)
    if days <= 1:
        return 0

    fst_buy = sec_buy = -0x80000000
    fst_sell = sec_sell = 0
    for i in range(days):
        price = prices[i]

        fst_buy = max(fst_buy, -price)
        fst_sell = max(fst_sell, fst_buy + price)

        sec_buy = max(sec_buy, fst_sell + -price)
        sec_sell = max(sec_sell, sec_buy + price)

    return sec_sell


if __name__ == '__main__':
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([3, 4, 2, 7, 6, 5]))
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([2, 7, 5, 3, 6, 1, 4, 2]))
    print(max_profit([1, 3, 2, 1, 3, 2, 1, 9]))

