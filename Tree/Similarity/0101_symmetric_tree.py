from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p or not q:
                return p is q
            return p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left)

        return dfs(root.left, root.right)


def test_is_symmetric():
    solution = Solution()
    assert solution.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))), 'wrong result'
    assert not solution.isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))), 'wrong result'


if __name__ == '__main__':
    test_is_symmetric()
