from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        x = root.val
        if x < p.val and x < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif x > p.val and x > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

    def lowestCommonAncestor1(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)

        if root is p or root is q:
            return root

        x = root.val
        if p.val < x < q.val:
            return root

        return self.lowestCommonAncestor(root.right, p, q) if x < p.val else self.lowestCommonAncestor(root.left, p, q)


def test_lowest_common_ancestor():
    solution = Solution()
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    assert solution.lowestCommonAncestor(root, root.left, root.right) == root, 'wrong result'


if __name__ == '__main__':
    test_lowest_common_ancestor()
