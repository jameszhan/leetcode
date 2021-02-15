"""
乘积最大子数组

给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

#### 示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

#### 示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""

"""
转移方程：
f max(i) = max {f max(i−1)×ai, f min(i−1)×ai, ai}
f min(i) = min {f max(i−1)×ai, f min(i−1)×ai, ai}
"""


def max_product(nums) -> int:
    fmax = fmin = ans = nums[0]
    for i in range(1, len(nums)):
        pre_fmax, pre_fmin = fmax, fmin
        fmax = max(pre_fmax * nums[i], pre_fmin * nums[i], nums[i])
        fmin = min(pre_fmax * nums[i], pre_fmin * nums[i], nums[i])
        ans = max(fmax, ans)
    return ans


if __name__ == '__main__':
    print(max_product([2, 3, -2, 4]))
    print(max_product([2, 3, -2, 4, 5, 1, -3]))
    print(max_product([-2, 3, 1]))
    print(max_product([-5, -3, 2, -4, 5, 1, -3]))

