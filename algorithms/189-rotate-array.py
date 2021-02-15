"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]


示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""


# def rotate(nums, k: int) -> None:
#     nums_len = len(nums)
#     if nums_len == k:
#         return
#     elif nums_len < k:
#         k %= nums_len
#
#     for i in range(k):
#         tmp = nums[-1]
#         for j in reversed(range(1, nums_len)):
#             nums[j] = nums[j - 1]
#         nums[0] = tmp

# def rotate(nums, k: int) -> None:
#     nums_len = len(nums)
#     if nums_len == k:
#         return
#     elif nums_len < k:
#         k %= nums_len
#
#     if k > nums_len // 2:
#         k = nums_len - k
#         for i in range(k):
#             tmp = nums[0]
#             for j in range(nums_len - 1):
#                 nums[j] = nums[j + 1]
#             nums[-1] = tmp
#     else:
#         for i in range(k):
#             tmp = nums[-1]
#             for j in reversed(range(1, nums_len)):
#                 nums[j] = nums[j - 1]
#             nums[0] = tmp


def rotate(nums, k: int) -> None:
    nums_len = len(nums)
    if nums_len == k:
        return
    elif nums_len < k:
        k %= nums_len

    tmp_nums = [nums[i] for i in range(nums_len - k, nums_len)]
    for i in reversed(range(k, nums_len)):
        nums[i] = nums[i - k]

    for i in range(len(tmp_nums)):
        nums[i] = tmp_nums[i]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    print(nums)

    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 1)
    print(nums)

    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 6)
    print(nums)

    nums = [-1, -100, 3, 99]
    rotate(nums, 2)
    print(nums)
