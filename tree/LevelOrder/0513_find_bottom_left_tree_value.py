from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node.right:
                dq.append(node.right)
            if node.left:
                dq.append(node.left)

        return node.val

    def findBottomLeftValue1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        res = list()
        dq = deque([root])
        while dq:
            vals = list()
            for _ in range(len(dq)):
                node = dq.popleft()
                vals.append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(vals)

        return res[-1][0]


def test_find_bottom_left_value():
    solution = Solution()
    assert solution.findBottomLeftValue(TreeNode(2, TreeNode(1), TreeNode(3))) == 1, 'wrong result'
    assert solution.findBottomLeftValue(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))) == 7, 'wrong result'


if __name__ == '__main__':
    test_find_bottom_left_value()
