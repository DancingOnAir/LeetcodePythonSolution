from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            return node.val + left[1] + right[1], max(left) + max(right)

        return max(dfs(root))

    def rob1(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            lr = lnr = rr = rnr = 0
            if node.left:
                lr, lnr = dfs(node.left)
            if node.right:
                rr, rnr = dfs(node.right)
            return node.val + lnr + rnr, max(lr, lnr) + max(rr, rnr)

        return max(dfs(root))


def test_rob():
    solution = Solution()
    assert solution.rob(TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))) == 7, 'wrong result'
    assert solution.rob(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))) == 9, 'wrong result'


if __name__ == '__main__':
    test_rob()
