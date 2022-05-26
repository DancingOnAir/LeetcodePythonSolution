from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        if root.left:
            root.left = self.pruneTree(root.left)
        if root.right:
            root.right = self.pruneTree(root.right)

        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root


def test_prune_tree():
    solution = Solution()

    node0 = TreeNode(0, TreeNode(0), TreeNode(1))
    root = TreeNode(1, None, node0)

    assert solution.pruneTree(root).val == 1, 'wrong result'
    assert solution.pruneTree(root).left is None, 'wrong result'
    assert solution.pruneTree(root).right.left is None, 'wrong result'


if __name__ == '__main__':
    test_prune_tree()
