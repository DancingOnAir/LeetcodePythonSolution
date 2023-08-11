from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


def test_search_bst():
    solution = Solution()
    assert solution.searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5) is None, 'wrong result'


if __name__ == '__main__':
    test_search_bst()
