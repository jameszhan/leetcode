"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

#### 示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
 
提示：皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自 百度百科 - 皇后 ）
"""


def solve_n_queens(n: int):
    c = []

    def dfs(a, k, predict):
        l = len(a)
        for i in range(l):
            a[k] = i
            if predict(a, k):
                if k == n - 1:
                    c.append(to_graph(a))
                else:
                    dfs(a, k + 1, predict)

    def check(a, k):
        for i in range(k):
            if a[k] == a[i] or abs(a[k] - a[i]) == k - i:
                return False
        return True

    def to_graph(a):
        graph = []
        l = len(a)
        for v in a:
            s = ''
            for i in range(l):
                if i == v:
                    s += 'Q'
                else:
                    s += '.'
            graph.append(s)
        return graph

    dfs([0 for _ in range(n)], 0, check)
    return c


if __name__ == '__main__':
    print(solve_n_queens(0))
    print(solve_n_queens(1))
    print(solve_n_queens(2))
    print(solve_n_queens(3))
    print(solve_n_queens(4))
    print(solve_n_queens(5))