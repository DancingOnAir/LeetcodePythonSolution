from typing import Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            cur_val = 0
            cur_depth = 0
            if node.left and node.val == node.left.val:
                cur_depth = max(cur_depth, left_depth)
                cur_val += left_depth

            if node.right and node.val == node.right.val:
                cur_depth = max(cur_depth, right_depth)
                cur_val += right_depth

            nonlocal res
            res = max(res, cur_val)
            return cur_depth + 1

        res = 0
        dfs(root)
        return res


def test_longest_univalue_path():
    solution = Solution()
    assert solution.longestUnivaluePath(TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))) == 2, 'wrong result'
    assert solution.longestUnivaluePath(TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5)))) == 2, 'wrong result'


if __name__ == '__main__':
    test_longest_univalue_path()
