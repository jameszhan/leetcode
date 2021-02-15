"""
搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4


示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""
from typing import List


# 根据旋转数组的特性，当元素不重复时，如果 nums[i] <= nums[j]，说明区间 [i,j] 是「连续递增」的。
def search(nums: List[int], target: int) -> int:
    nums_len = len(nums)
    if nums_len <= 0:
        return -1
    elif nums_len == 1:
        return 0 if target == nums[0] else -1
    else:
        i, j = 0, nums_len - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid

            if nums[i] <= nums[mid]:                    # [i, mid] 连续递增
                if nums[i] <= target <= nums[mid]:
                    j = mid -1
                else:
                    i = mid + 1
            else:                                       # [mid, j] 连续递增
                if nums[mid] <= target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        return -1


if __name__ == '__main__':
    print(search([4, 5, 6, 7, 0, 1, 2], 0))
    print(search([4, 5, 6, 7, 0, 1, 2], 3))
