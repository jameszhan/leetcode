"""
两数之和 IV - 输入 BST

给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

#### 案例 1:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

#### 案例 2:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def add_tree_node(node: TreeNode, v):
    if node is None:
        return TreeNode(v)
    else:
        if v <= node.val:
            if node.left is None:
                node.left = TreeNode(v)
            else:
                add_tree_node(node.left, v)
        else:
            if node.right is None:
                node.right = TreeNode(v)
            else:
                add_tree_node(node.right, v)


def build_tree(nums):
    node = TreeNode(nums[0])
    for i in range(1, len(nums)):
        num = nums[i]
        add_tree_node(node, num)
    return node


def find_target(root: TreeNode, k: int) -> bool:
    def inorder(node, handle):
        if node is not None:
            inorder(node.left, handle)
            handle(node.val)
            inorder(node.right, handle)

    candidates = {}

    def find_candidates(v):
        candidates[k - v] = v

    inorder(root, find_candidates)

    result = []

    def check_candidates(v):
        if v in candidates and v != candidates[v]:
            result.append(v)

    inorder(root, check_candidates)

    return len(result) > 0


if __name__ == '__main__':
    tree = build_tree([5, 3, 6, 2, 4, 7])
    print(find_target(tree, 9))
    print(find_target(tree, 28))

    tree2 = build_tree([1])
    print(find_target(tree2, 2))

