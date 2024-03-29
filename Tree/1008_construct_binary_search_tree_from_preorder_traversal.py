import bisect
from typing import List, Optional
from bisect import bisect_right


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = bisect_right(preorder, root.val)
        root.left = self.bstFromPreorder(preorder[1: i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

    # recursive
    def bstFromPreorder2(self, preorder: List[int]) -> Optional[TreeNode]:
        def build_tree(arr: List[int], val: int):
            if not arr or arr[-1] > val:
                return None
            node = TreeNode(arr.pop())
            node.left = build_tree(arr, node.val)
            node.right = build_tree(arr, val)
            return node
        return build_tree(preorder[::-1], float('inf'))

    # recursive
    def bstFromPreorder1(self, preorder: List[int]) -> Optional[TreeNode]:
        # def helper(order):
        #     if not order:
        #         return None
        #     if len(order) == 1:
        #         return TreeNode(order[0])
        #     root = TreeNode(order[0])
        #     for i, val in enumerate(order[1:]):
        #         if val > root.val:
        #             root.left = helper(order[1: i+1])
        #             root.right = helper(order[i+1:])
        #             return root
        #     root.left = helper(order[1:])
        #     return root

        # return helper(preorder)
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        root.left = self.bstFromPreorder(preorder[1: i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root


def test_bst_from_preorder():
    solution = Solution()
    root = solution.bstFromPreorder([8, 5, 1, 7, 10, 12])
    assert root.val == 8, 'wrong result'
    assert root.left.val == 5, 'wrong result'
    assert root.right.val == 10, 'wrong result'


if __name__ == '__main__':
    test_bst_from_preorder()
