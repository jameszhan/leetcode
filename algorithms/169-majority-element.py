"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3

示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""


def majority_element(nums) -> int:
    d = {}
    for n in nums:
        if n in d:
            d[n] = d[n] + 1
        else:
            d[n] = 1

    ans = nums[0]
    for k in d:
        if d[k] > d[ans]:
            ans = k
    return ans


# 因为最多的元素超过半数，所以可以一次遍历数组找出来
def majority_element2(nums) -> int:
    ans = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if ans == nums[i]:
            count += 1
        else:
            count -= 1
            if count == 0:
                ans = nums[i + 1]
    return ans


if __name__ == '__main__':
    print(majority_element([3, 2, 3]))
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
    print(majority_element2([3, 2, 3]))
    print(majority_element2([2, 2, 1, 1, 1, 2, 2]))
