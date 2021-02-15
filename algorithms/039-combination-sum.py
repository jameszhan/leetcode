"""
组合总和

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]


示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    answers = []
    candidates_len = len(candidates)

    def solve(expected: int, start: int, ans: List[int]):
        if expected < 0:
            return
        elif expected == 0:
            answers.append(ans.copy())
        else:
            for i in range(start, candidates_len):
                ans.append(candidates[i])
                solve(expected - candidates[i], i, ans)
                ans.pop()
                # del(ans[-1])

    if candidates_len > 0:
        answer = []
        solve(target, 0, answer)
    return answers


if __name__ == '__main__':
    print(combination_sum([], 7))
    print(combination_sum([7], 7))
    print(combination_sum([2, 3, 6, 7], 7))
    print(combination_sum([2, 3, 5], 8))

