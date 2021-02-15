"""
不同的二叉搜索树

给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


"""
catalan数 = C(2n,n) / (n+1)

问题是计算不同二叉搜索树的个数。为此，我们可以定义两个函数：

G(n): 长度为n的序列的不同二叉搜索树个数。

F(i,n): 以i为根的不同二叉搜索树个数(1≤i≤n)。

可见，G(n) 是我们解决问题需要的函数。

稍后我们将看到，
G(n) 可以从 F(i,n) 得到，而 F(i,n) 又会递归的依赖于 G(n)。

首先，根据上一节中的思路，不同的二叉搜索树的总数 G(n)，是对遍历所有 i (1 <= i <= n) 的 F(i,n) 之和。换而言之：

G(n) = ∑ F(i,n)                      (1)

特别的，对于边界情况，当序列长度为 1 （只有根）或为 0 （空树）时，只有一种情况。亦即：G(0)=1, G(1)=1
F(i,n) = G(i−1)⋅G(n−i)               (2)

将公式 (1)，(2) 结合，可以得到 G(n) 的递归表达公式：
G(n) = G(i−1)⋅G(n−i)                 (3)

G(n) = G(0)∗G(n−1) + G(1)∗(n−2) + ... + G(n−1)∗G(0)
"""


def num_trees(n: int) -> int:
    if n <= 0:
        return 1
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    return dp[n]


def num_trees2(n: int) -> int:
    if n < 2:
        return 1
    ans = 0
    for i in range(n):
        ans += num_trees2(i) * num_trees2(n - i - 1)
    return ans


def num_trees3(m: int) -> int:
    cache = {0: 1, 1: 1}

    def solve(n):
        if n < 2:
            return 1
        ans = 0
        for i in range(n):
            if i not in cache:
                cache[i] = solve(i)
            if n - i - 1 not in cache:
                cache[n - i - 1] = solve(n - i - 1)
            ans += cache[i] * cache[n - i - 1]
        cache[n] = ans
        return ans

    return solve(m)


if __name__ == '__main__':
    print(num_trees(0))
    print(num_trees(1))
    print(num_trees(2))
    print(num_trees(3))
    print(num_trees(10))
    print(num_trees2(19))

    print(num_trees2(0))
    print(num_trees2(1))
    print(num_trees2(2))
    print(num_trees2(3))
    print(num_trees2(10))
    print(num_trees2(19))

    print(num_trees3(0))
    print(num_trees3(1))
    print(num_trees3(2))
    print(num_trees3(3))
    print(num_trees3(10))
    print(num_trees3(19))