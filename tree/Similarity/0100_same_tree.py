from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def test_is_same_tree():
    solution = Solution()
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))), 'wrong result'
    assert not solution.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))), 'wrong result'
    assert not solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))), 'wrong result'


if __name__ == '__main__':
    test_is_same_tree()



