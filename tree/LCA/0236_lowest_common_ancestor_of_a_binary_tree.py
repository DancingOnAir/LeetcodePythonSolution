from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        return right


def test_lowest_common_ancestor():
    solution = Solution()
    root = TreeNode(1, TreeNode(2))
    assert solution.lowestCommonAncestor(root, root, root.left) == root, 'wrong result'


if __name__ == '__main__':
    test_lowest_common_ancestor()

