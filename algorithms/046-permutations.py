"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。


#### 示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


def permute(nums):
    ret = []
    def dfs(a, k, predict):
        n = len(a)
        for i in range(n):
            a[k] = i
            if predict(a, k):
                if k == n - 1:
                    ret.append(list(map(lambda i: nums[i], a)))
                else:
                    dfs(a, k + 1, predict)

    def check(a, k):
        for i in range(k):
            if a[i] == a[k]:
                return False
        return True

    l = len(nums)
    dfs([0 for _ in range(l)], 0, check)
    return ret


if __name__ == '__main__':
    print(permute([1, 2, 3]))