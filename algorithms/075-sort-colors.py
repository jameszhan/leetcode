"""
颜色分类

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""
from typing import List


def sort_colors(nums: List[int]) -> None:
    nums_len = len(nums)
    pivot = 1
    i, l, r = 0, 0, nums_len - 1
    while i <= r:
        if nums[i] < pivot:
            if i != l:
                nums[i], nums[l] = nums[l], nums[i]
            l += 1
            i += 1
        elif nums[i] > pivot:
            if i != r:
                nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        else:
            i += 1

    print(nums)


if __name__ == '__main__':
    sort_colors([])
    sort_colors([1])
    sort_colors([0, 1, 0])
    sort_colors([1, 2, 0])
    sort_colors([2, 0, 1])
    sort_colors([2, 1, 0])
    sort_colors([2, 0, 2, 1, 1, 0])
    sort_colors([2, 0, 1, 1, 1, 1])
    sort_colors([1, 0, 2, 0, 1, 1, 1, 1])


