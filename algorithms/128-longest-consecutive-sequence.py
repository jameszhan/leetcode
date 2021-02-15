"""
最长连续序列

给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

#### 示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""


def longest_consecutive(nums) -> int:
    dp = {}
    for num in nums:
        dp[num] = 1

    longest = 0
    for num in nums:
        if num - 1 not in dp:
            current_len = 1
            next_num = num + 1
            while next_num in dp:
                current_len += 1
                next_num += 1

            longest = max(current_len, longest)

    return longest


if __name__ == '__main__':
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))



