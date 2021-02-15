"""
打家劫舍 II

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

#### 示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。


#### 示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""


def rob(numbers) -> int:

    def do_rob(nums):
        nums_len = len(nums)
        rob_amount = nums[0]
        stop_amount = 0
        for i in range(1, nums_len):
            pre_rob_amount = rob_amount
            rob_amount = max(rob_amount, stop_amount + nums[i])
            stop_amount = max(pre_rob_amount, stop_amount)

        return rob_amount

    length = len(numbers)
    if length <= 0:
        return 0
    elif length == 1:
        return numbers[0]
    else:
        return max(do_rob(numbers[1:]), do_rob(numbers[0:-1]))


if __name__ == '__main__':
    print(rob([]))
    print(rob([2]))
    print(rob([1, 2, 3, 1]))
    print(rob([2, 3, 2]))
