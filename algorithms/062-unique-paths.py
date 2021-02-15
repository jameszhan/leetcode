"""
不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右


示例 2:

输入: m = 7, n = 3
输出: 28
 
提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9
"""


def unique_paths(m: int, n: int) -> int:
    if m <= 1 or n <= 1:
        return 1
    else:
        return unique_paths(m - 1, n) + unique_paths(m, n - 1)


def unique_paths2(m: int, n: int) -> int:
    cache = {}
    for i in range(m + 1):
        cache[i] = {}

    def solve(m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        else:
            if n not in cache[m - 1]:
                cache[m - 1][n] = solve(m - 1, n)
            if n - 1 not in cache[m]:
                cache[m][n - 1] = solve(m, n - 1)

            return cache[m - 1][n] + cache[m][n - 1]

    return solve(m, n)


def unique_paths3(m: int, n: int) -> int:
    cache = {}

    def solve(m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        else:
            if (m - 1, n) not in cache:
                cache[(m - 1, n)] = solve(m - 1, n)
            if (m, n - 1) not in cache:
                cache[(m, n - 1)] = solve(m, n - 1)

            return cache[(m - 1, n)] + cache[(m, n - 1)]

    return solve(m, n)


if __name__ == '__main__':
    print(unique_paths(3, 2))
    print(unique_paths(7, 3))
    print(unique_paths(10, 10))
    # print(unique_paths(23, 12))

    print(unique_paths2(3, 2))
    print(unique_paths2(7, 3))
    print(unique_paths2(10, 10))
    print(unique_paths2(23, 12))

    print(unique_paths3(3, 2))
    print(unique_paths3(7, 3))
    print(unique_paths3(10, 10))
    print(unique_paths3(23, 12))