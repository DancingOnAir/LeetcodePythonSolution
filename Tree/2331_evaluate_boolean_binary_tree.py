from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left == root.right:
            return root.val == 1

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)


def test_evaluate_tree():
    solution = Solution()
    assert solution.evaluateTree(TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))), 'wrong result'
    assert not solution.evaluateTree(TreeNode(0)), 'wrong result'


if __name__ == '__main__':
    test_evaluate_tree()
