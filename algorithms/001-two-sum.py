"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

#### 示例:

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def two_sum(nums, target: int):
    candidates = {}
    for i, n in enumerate(nums):
        # if target >= n:
        candidates[target - n] = i
    for i, n in enumerate(nums):
        if n in candidates and i != candidates[n]:
            return [i, candidates[n]]


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([11, 7, 15, 2], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([0, 4, 3, 0], 0))
    print(two_sum([-1, -2, -3, -4, -5], -8))
