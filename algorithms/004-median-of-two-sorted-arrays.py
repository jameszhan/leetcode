"""
寻找两个正序数组的中位数

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0


示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    a_len, b_len = len(nums1), len(nums2)
    max_len = a_len + b_len
    mid = max_len // 2

    i, j, k = 0, 0, 0
    pre_val, curr_val = 0, 0
    while k <= mid:
        pre_val = curr_val
        if i < a_len and j < b_len:
            if nums1[i] < nums2[j]:
                curr_val = nums1[i]
                i += 1
            else:
                curr_val = nums2[j]
                j += 1
        elif i < a_len:
            curr_val = nums1[i]
            i += 1
        elif j < b_len:
            curr_val = nums2[j]
            j += 1
        k += 1

    if max_len % 2 == 0:
        return (pre_val + curr_val) / 2
    else:
        return curr_val


if __name__ == '__main__':
    print(find_median_sorted_arrays([1, 3], [2]))
    print(find_median_sorted_arrays([1, 2], [3, 4]))