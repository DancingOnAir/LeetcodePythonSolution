from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        while q:
            pre, q = q, [child for node in q for child in (node.left, node.right) if child]
        return sum(node.val for node in pre)

    def deepestLeavesSum1(self, root: Optional[TreeNode]) -> int:
        def helper(node, depth):
            if not node:
                return
            self.deepest = max(self.deepest, depth)
            self.m[depth] += node.val
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)

        self.deepest = 0
        self.m = defaultdict(int)
        helper(root, 0)
        return self.m[self.deepest]


def test_deepest_leaves_sum():
    solution = Solution()

    root1 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))
    assert solution.deepestLeavesSum(root1) == 15, 'wrong result'

    root2 = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))),
                     TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
    assert solution.deepestLeavesSum(root2) == 19, 'wrong result'


if __name__ == '__main__':
    test_deepest_leaves_sum()
