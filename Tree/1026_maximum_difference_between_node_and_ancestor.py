from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, arr):
            if not node:
                return

            arr.append(node.val)
            mx = max(arr)
            mi = min(arr)
            self.res = max(self.res, mx - mi)
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


