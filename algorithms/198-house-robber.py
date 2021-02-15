"""
打家劫舍

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

#### 示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

#### 示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

#### 提示：

0 <= nums.length <= 100
0 <= nums[i] <= 400
"""


def rob(nums) -> int:
    nums_len = len(nums)
    if nums_len < 1:
        return 0
    rob_amount = nums[0]
    stop_amount = 0
    for i in range(1, nums_len):
        pre_rob_amount = rob_amount
        rob_amount = max(rob_amount, stop_amount + nums[i])
        stop_amount = max(pre_rob_amount, stop_amount)

    return rob_amount


if __name__ == '__main__':
    print(rob([1, 2, 3, 1]))
    print(rob([2, 7, 9, 3, 1]))
