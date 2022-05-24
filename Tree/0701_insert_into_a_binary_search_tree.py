from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

    # recursive
    def insertIntoBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(root: Optional[TreeNode], parent: Optional[TreeNode]):
            if not root:
                if not parent:
                    return

                if parent.val < val:
                    parent.right = TreeNode(val)
                else:
                    parent.left = TreeNode(val)
                return
            if root.val < val:
                helper(root.right, root)
            else:
                helper(root.left, root)

        helper(root, None)
        return root if root else TreeNode(val)


def test_insert_into_bst():
    solution = Solution()

    node2 = TreeNode(2, TreeNode(1), TreeNode(3))
    root = TreeNode(4, node2, TreeNode(7))
    assert solution.insertIntoBST(root, 5).val == 4, 'wrong result'

    root = None
    assert solution.insertIntoBST(root, 5).val == 5, 'wrong result'


if __name__ == '__main__':
    test_insert_into_bst()
