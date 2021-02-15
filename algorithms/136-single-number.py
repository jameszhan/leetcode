"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

#### 示例 1:

输入: [2,2,1]
输出: 1

#### 示例 2:

输入: [4,1,2,1,2]
输出: 4
"""


def single_number(nums) -> int:
    t = 0
    for x in nums:
        t ^= x
    return t


if __name__ == '__main__':
    print(single_number([2, 2, 1]))
    print(single_number([4, 1, 2, 1, 2]))