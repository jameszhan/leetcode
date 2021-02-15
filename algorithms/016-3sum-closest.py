"""
最接近的三数之和

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

#### 示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 
#### 提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""
from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    nums_len = len(nums)
    if nums_len < 3:
        return 0
    elif nums_len == 3:
        return sum(nums)
    else:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        if ans == target:
            return ans

        for i in range(nums_len):
            left, right = i + 1, nums_len - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if abs(target - tmp) < abs(target - ans):
                    ans = tmp

                if tmp > target:
                    right -= 1
                elif tmp < target:
                    left += 1
                else:
                    return ans

        return ans


if __name__ == '__main__':
    print(three_sum_closest([-1, 2, 1, -4], 1))
