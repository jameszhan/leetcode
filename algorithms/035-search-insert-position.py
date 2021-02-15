"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2

示例 2:

输入: [1,3,5,6], 2
输出: 1

示例 3:

输入: [1,3,5,6], 7
输出: 4


示例 4:

输入: [1,3,5,6], 0
输出: 0
"""


def search_insert(nums, target) -> int:
    nums_len = len(nums)
    if nums_len < 1:
        return 0

    left, right = 0, nums_len - 1
    if nums[-1] < target:
        return nums_len
    elif nums[0] > target:
        return 0
    else:
        while left < right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        return left if nums[left] >= target else left + 1


if __name__ == '__main__':
    print(search_insert([1], 1))         # 1
    print(search_insert([1, 3], 2))         # 1
    print(search_insert([1, 3, 5, 6], 5))   # 2
    print(search_insert([1, 3, 5, 6], 2))   # 1
    print(search_insert([1, 3, 5, 6], 7))   # 4
    print(search_insert([1, 3, 5, 6], 0))   # 0
