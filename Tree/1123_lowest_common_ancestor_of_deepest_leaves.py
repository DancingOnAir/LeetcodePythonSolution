from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def LCA(root, nodes):
            if not root or root in nodes:
                return root
            left = LCA(root.left, nodes)
            right = LCA(root.right, nodes)

            if left and right:
                return root
            return left if left else right

        level = [root]
        while level:
            cur = [child for node in level for child in [node.left, node.right] if child]
            if not cur:
                break
            level = cur
        return LCA(root, set(level))


def test_lca_deepest_leaves():
    solution = Solution()

    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    assert solution.lcaDeepestLeaves(root).val == 2, 'wrong result'


if __name__ == '__main__':
    test_lca_deepest_leaves()

