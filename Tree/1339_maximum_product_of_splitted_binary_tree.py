from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def preorder(node, flag):
            if not node:
                return 0

            if flag:
                self.nodes.append(node)
            left = preorder(node.left, flag)
            right = preorder(node.right, flag)
            return left + right + node.val

        self.nodes = list()
        total = preorder(root, True)
        res = 0
        for node in self.nodes:
            subtree = preorder(node, False)
            res = max(res, subtree * (total - subtree))

        return res % (10 ** 9 + 7)


def test_max_product():
    solution = Solution()
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    assert solution.maxProduct(root1) == 110, 'wrong result'
    root2 = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), TreeNode(6))))
    assert solution.maxProduct(root2) == 90, 'wrong result'


if __name__ == '__main__':
    test_max_product()
