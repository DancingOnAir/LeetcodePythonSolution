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
        def find_deepest_level(node):
            if not node:
                return 0
            return max(find_deepest_level(node.left), find_deepest_level(node.right)) + 1

        def get_deepest_sum(node, i):
            if not node:
                return 0

            if depth == i:
                self.res += node.val
            get_deepest_sum(node.left, i + 1)
            get_deepest_sum(node.right, i + 1)

        self.res = 0
        depth = find_deepest_level(root)
        get_deepest_sum(root, 1)
        return self.res

    # level order
    def deepestLeavesSum2(self, root: Optional[TreeNode]) -> int:
        q = [root]
        while q:
            pre, q = q, [child for node in q for child in (node.left, node.right) if child]
        return sum(node.val for node in pre)

    # preorder + defaultdict
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
