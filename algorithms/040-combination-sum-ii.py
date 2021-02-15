"""
组合总和 II

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]


示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""
from typing import List


def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    answers = []
    candidates_len = len(candidates)
    candidates.sort()

    def solve(expected: int, start: int, ans: List[int]):
        if expected < 0:
            return
        elif expected == 0:
            if ans not in answers:
                answers.append(ans.copy())
        else:
            for i in range(start, candidates_len):
                ans.append(candidates[i])
                solve(expected - candidates[i], i + 1, ans)
                ans.pop()
                # del(ans[-1])

    if candidates_len > 0:
        answer = []
        solve(target, 0, answer)
    return answers


if __name__ == '__main__':
    print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(combination_sum2([2, 5, 2, 1, 2], 5))
    print(combination_sum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27))
