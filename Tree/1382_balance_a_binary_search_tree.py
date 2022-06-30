from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.tree.append(node.val)
            inorder(node.right)

        self.tree = list()
        inorder(root)


        pass


def test_balance_bst():
    solution = Solution()

    root1 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    root2 = solution.balanceBST(root1)
    assert root2.val == 2, 'wrong result'


if __name__ == '__main__':
    test_balance_bst()
