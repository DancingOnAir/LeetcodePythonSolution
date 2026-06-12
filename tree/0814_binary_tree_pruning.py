from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # postorder
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return True
            left, right = dfs(node.left), dfs(node.right)
            if left:
                node.left = None
            if right:
                node.right = None
            return left and right and node.val == 0

        return root if not dfs(root) else None

    # postorder
    def pruneTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
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
