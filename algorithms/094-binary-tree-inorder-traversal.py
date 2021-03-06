"""
二叉树的中序遍历

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_traversal(root: TreeNode) -> List[int]:

    def travel(node: TreeNode, arr: List[int]) -> None:
        if node is not None:
            travel(node.left, arr)
            arr.append(node.val)
            travel(node.right, arr)

    ans = []
    travel(root, ans)
    return ans
