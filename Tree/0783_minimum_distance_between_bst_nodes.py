from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        bst = list()
        stk = [root]
        while stk:
            node = stk[-1]
            while node:
                stk.append(node.left)
                node = node.left
            stk.pop()

            if stk:
                node = stk.pop()
                bst.append(node.val)
                stk.append(node.right)

        res = float('inf')
        for a, b in zip(bst, bst[1:]):
            res = min(res, abs(a - b))
            if res == 1:
                break
        return res


def test_min_diff_in_bst():
    solution = Solution()
    node48 = TreeNode(48, TreeNode(12), TreeNode(49))
    root = TreeNode(1, TreeNode(0), node48)
    assert solution.minDiffInBST(root) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_diff_in_bst()
