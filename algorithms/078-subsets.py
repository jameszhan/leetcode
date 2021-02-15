"""
子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from typing import List


def subsets02(nums: List[int]) -> List[List[int]]:
    nums_len = len(nums)
    answers = []

    def solve(start: int, ans: List[int]) -> None:
        answer = [nums[i] for i in ans]
        answer.sort()
        if answer not in answers:
            answers.append(answer)
        for i in range(start, nums_len):
            if i not in ans:
                ans.append(i)
                solve(start + 1, ans)
                ans.pop()

    solve(0, [])
    return answers


def to_bits(x, m):
    ret = []
    for k in range(m):
        ret.append(x & 1)
        x = x >> 1
    ret.reverse()
    return ret


def subsets03(nums: List[int]) -> List[List[int]]:
    ans, n = [], len(nums)
    for i in range(1 << n):
        selector = to_bits(i, n)
        curr = []
        for j in range(n):
            if selector[j] == 1:
                curr.append(nums[j])
        ans.append(curr)
    return ans


def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = []
    for i in range(1 << n):
        track = []
        for j in range(n):
            if (i >> j) & 1 == 1:
                track.append(nums[j])
        ans.append(track)

    return ans


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
    print(subsets([0]))