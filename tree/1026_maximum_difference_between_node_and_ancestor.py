from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, lo, hi):
            if not node:
                return hi - lo
            hi = max(hi, node.val)
            lo = min(lo, node.val)
            # 这里不需要比较hi - lo的值，因为可以把一条路径走到底，直接比较这条路径上的最小值和最大值即可。
            return max(helper(node.left, lo, hi), helper(node.right, lo, hi))

        if not root:
            return 0
        return helper(root, root.val, root.val)

    def maxAncestorDiff1(self, root: Optional[TreeNode]) -> int:
        def dfs(node, arr):
            if not node:
                return

            arr.append(node.val)
            mx = max(arr)
            mn = min(arr)
            self.res = max(self.res, mx - mn)
            dfs(node.left, arr)
            dfs(node.right, arr)
            arr.pop()

        self.res = float('-inf')
        dfs(root, [])
        return self.res


def test_max_ancestor_diff():
    solution = Solution()

    root1 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
    assert solution.maxAncestorDiff(root1) == 7, 'wrong result'

    root2 = TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3))))
    assert solution.maxAncestorDiff(root2) == 3, 'wrong result'


if __name__ == '__main__':
    test_max_ancestor_diff()


