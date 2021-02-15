"""
不同的二叉搜索树 II

给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

提示：

0 <= n <= 8
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generate_trees(n: int) -> List[TreeNode]:
    def do_generate_trees(start, end):
        if start > end:
            return [None]

        ans = []
        for i in range(start, end + 1):
            left_trees = do_generate_trees(start, i - 1)
            right_trees = do_generate_trees(i + 1, end)

            for l in left_trees:
                for r in right_trees:
                    tree = TreeNode(i + 1)
                    tree.left = l
                    tree.right = r
                    ans.append(tree)

        return ans

    if n == 0:
        return []
    else:
        return do_generate_trees(0, n - 1)


if __name__ == '__main__':
    print(generate_trees(3))
