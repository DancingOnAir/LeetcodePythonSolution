from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val


def test_check_tree():
    solution = Solution()
    left = TreeNode(4)
    right = TreeNode(6)
    root = TreeNode(10, left, right)

    assert solution.checkTree(root), 'wrong result'


if __name__ == '__main__':
    test_check_tree()
