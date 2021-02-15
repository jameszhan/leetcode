"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶


示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution:

    def climb_stairs(self, m: int) -> int:
        cache = {}

        def solve(n):
            if n <= 1:
                return 1
            elif n == 2:
                return 2
            else:
                if n - 2 in cache:
                    n_2 = cache[n - 2]
                else:
                    n_2 = solve(n - 2)
                    cache[n - 2] = n_2

                if n - 1 in cache:
                    n_1 = cache[n - 1]
                else:
                    n_1 = solve(n - 1)
                    cache[n - 1] = n_1

                cache[n] = n_1 + n_2
                return n_1 + n_2
        return solve(m)


def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb_stairs(n - 1) + climb_stairs(n - 2)


if __name__ == '__main__':
    print(climb_stairs(0))
    print(climb_stairs(1))
    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(6))
    print(climb_stairs(10))
    print(climb_stairs(12))
    print(climb_stairs(30))

    solution = Solution()
    print(solution.climb_stairs(0))
    print(solution.climb_stairs(1))
    print(solution.climb_stairs(2))
    print(solution.climb_stairs(3))
    print(solution.climb_stairs(6))
    print(solution.climb_stairs(10))
    print(solution.climb_stairs(12))
    print(solution.climb_stairs(38))

