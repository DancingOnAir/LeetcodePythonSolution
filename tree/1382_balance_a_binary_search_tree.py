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
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        def build(l, r):
            if l > r:
                return None
            m = l + (r - l) // 2
            node = TreeNode(self.tree[m])
            node.left = build(l, m - 1)
            node.right = build(m + 1, r)
            return node

        self.tree = inorder(root)
        return build(0, len(self.tree) - 1)

    def balanceBST1(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.tree.append(node.val)
            inorder(node.right)

        def helper(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            node = TreeNode(arr[mid])
            node.left = helper(arr[: mid])
            node.right = helper(arr[mid + 1:])
            return node

        self.tree = list()
        inorder(root)
        return helper(self.tree)


def test_balance_bst():
    solution = Solution()

    root1 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    root2 = solution.balanceBST(root1)
    assert root2.val == 3, 'wrong result'


if __name__ == '__main__':
    test_balance_bst()
