"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""


def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j, p = m - 1, n - 1, m + n -1
    while i >= 0 and j >= 0:
        if nums2[j] > nums1[i]:
            nums1[p] = nums2[j]
            j -= 1
        else:
            nums1[p] = nums1[i]
            i -= 1
        p -= 1
    while i >= 0:
        nums1[p] = nums1[i]
        p -= 1
        i -= 1

    while j >= 0:
        nums1[p] = nums2[j]
        p -= 1
        j -= 1


if __name__ == '__main__':
    print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print(merge([1, 2, 3, 0, 0, 0, 0], 3, [1, 2, 2, 4], 4))
    print(merge([5, 6, 7, 0, 0, 0], 3, [1, 2, 3], 3))


