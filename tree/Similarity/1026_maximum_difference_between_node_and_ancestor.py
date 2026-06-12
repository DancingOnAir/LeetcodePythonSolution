from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # bottom-up
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        # return value: min, max
        def dfs(node):
            if not node:
                return float('inf'), float('-inf')

            mn = mx = node.val
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)
            mn = min(mn, left_min, right_min)
            mx = max(mx, left_max, right_max)

            nonlocal res
            res = max(res, mx - node.val, node.val - mn)
            return mn, mx

        res = 0
        dfs(root)
        return res

    # top-down
    def maxAncestorDiff1(self, root: Optional[TreeNode]) -> int:
        def dfs(node, lo, hi):
            if not node:
                return hi - lo
            hi = max(hi, node.val)
            lo = min(lo, node.val)
            return max(dfs(node.left, lo, hi), dfs(node.right, lo, hi))

        if not root:
            return 0
        return dfs(root, root.val, root.val)


def test_max_ancestor_diff():
    solution = Solution()
    assert solution.maxAncestorDiff(TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))) == 7, 'wrong result'
    assert solution.maxAncestorDiff(TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3))))) == 3, 'wrong result'


if __name__ == '__main__':
    test_max_ancestor_diff()
