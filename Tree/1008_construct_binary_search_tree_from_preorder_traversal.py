from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(order):
            if not order:
                return None
            if len(order) == 1:
                return TreeNode(order[0])
            root = TreeNode(order[0])
            for i, val in enumerate(order[1:]):
                if val > root.val:
                    root.left = helper(order[1: i+1])
                    root.right = helper(order[i+1:])
                    return root
            root.left = helper(order[1:])
            return root

        return helper(preorder)


def test_bst_from_preorder():
    solution = Solution()
    root = solution.bstFromPreorder([8, 5, 1, 7, 10, 12])
    assert root.val == 8, 'wrong result'
    assert root.left.val == 5, 'wrong result'
    assert root.right.val == 10, 'wrong result'


if __name__ == '__main__':
    test_bst_from_preorder()
