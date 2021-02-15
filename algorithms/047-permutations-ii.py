."""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

#### 示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def permute_unique(nums):
    cache = []

    def dfs(a, k, predict):
        n = len(a)
        for i in range(n):
            a[k] = i
            if predict(a, k):
                if k == n - 1:
                    target = list(map(lambda x: nums[x], a))
                    if target not in cache:
                        cache.append(target)
                else:
                    dfs(a, k + 1, predict)

    def check(a, k):
        for i in range(k):
            if a[i] == a[k]:
                return False
        return True

    dfs([0 for _ in range(len(nums))], 0, check)
    return cache


if __name__ == '__main__':
    print(permute_unique([1, 1, 2]))
