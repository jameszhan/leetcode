"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

#### 示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
 

提示：皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或七步，可进可退。（引用自 百度百科 - 皇后 ）
"""


def total_n_queens(n: int) -> int:
    total = []

    def dfs(a, k, predict):
        l = len(a)
        for i in range(l):
            a[k] = i
            if predict(a, k):
                if k == n - 1:
                    total.append(0)
                else:
                    dfs(a, k + 1, predict)

    def check(a, k):
        for i in range(k):
            if a[k] == a[i] or abs(a[k] - a[i]) == k - i:
                return False
        return True

    dfs([0 for _ in range(n)], 0, check)
    return len(total)


if __name__ == '__main__':
    print(total_n_queens(0))
    print(total_n_queens(1))
    print(total_n_queens(2))
    print(total_n_queens(3))
    print(total_n_queens(4))
    print(total_n_queens(5))