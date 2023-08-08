from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # stack
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = list()
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return -1

    # recursive
    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(node):
            if not node:
                return

            inorder_traversal(node.left)
            nonlocal k
            k -= 1
            if k == 0:
                nonlocal res
                res = node.val
            inorder_traversal(node.right)

        res = 0
        inorder_traversal(root)
        return res


def test_kth_smallest():
    solution = Solution()
    assert solution.kthSmallest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1) == 1, 'wrong result'
    assert solution.kthSmallest(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 3) == 3, 'wrong result'


if __name__ == '__main__':
    test_kth_smallest()
