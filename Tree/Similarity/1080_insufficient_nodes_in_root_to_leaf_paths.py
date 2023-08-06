from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left= left
        self.right = right


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        limit -= root.val
        if root.left is root.right:
            return root if limit <= 0 else None

        if root.left:
            root.left = self.sufficientSubset(root.left, limit)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit)
        return root if root.left or root.right else None


def test_sufficient_subset():
    solution = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(-5)), TreeNode(-3, TreeNode(4)))
    assert solution.sufficientSubset(root, -1).left is None, 'wrong result'


if __name__ == '__main__':
    test_sufficient_subset()
