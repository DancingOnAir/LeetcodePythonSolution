from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]):
        def dfs(node):
            if not node:
                return 0, 0

            l = dfs(node.left)
            r = dfs(node.right)

            select = l[1] + r[1] + node.val
            unselect = max(l) + max(r)

            return select, unselect

        return max(dfs(root))


def test_rob():
    solution = Solution()
    assert solution.rob(TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))) == 7, 'wrong result'
    assert solution.rob(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))) == 9, 'wrong result'


if __name__ == '__main__':
    test_rob()


