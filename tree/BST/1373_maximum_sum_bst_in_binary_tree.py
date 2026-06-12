from typing import Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0

        def postorder_traversal(node):
            if node is None:
                return inf, -inf, 0

            left_min, left_max, left_sum = postorder_traversal(node.left)
            right_min, right_max, right_sum = postorder_traversal(node.right)
            if node.val <= left_max or node.val >= right_min:
                return -inf, inf, 0

            nonlocal res
            res = max(res, left_sum + right_sum + node.val)
            return min(left_min, node.val), max(right_max, node.val), left_sum + right_sum + node.val

        postorder_traversal(root)
        return res


def test_max_sum_bst():
    solution = Solution()
    assert solution.maxSumBST(TreeNode(1, TreeNode(4, TreeNode(2), TreeNode(4)), TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6))))) == 20, 'wrong result'
    assert solution.maxSumBST(TreeNode(4, TreeNode(3, TreeNode(1), TreeNode(2)))) == 2, 'wrong result'
    assert solution.maxSumBST(TreeNode(-4, TreeNode(-2), TreeNode(-5))) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_sum_bst()
