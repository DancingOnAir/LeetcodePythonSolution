from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return None, 0
            left, h1 = helper(node.left)
            right, h2 = helper(node.right)
            if h1 > h2:
                return left, h1 + 1
            if h1 < h2:
                return right, h2 + 1
            return node, h1 + 1

        return helper(root)[0]

    def lcaDeepestLeaves2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # get subtree deepest depth
        def helper(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            if left == right == self.deepest:
                self.lca = node
            return max(left, right)

        self.deepest = 0
        self.lca = None
        helper(root, 0)
        return self.lca

    def lcaDeepestLeaves1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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

