from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        dq = deque([(root, 1)])

        while len(dq) > 0:
            sz = len(dq)
            if sz > 1:
                res = max(res, dq[-1][1] - dq[0][1] + 1)
            while sz:
                x = dq.popleft()
                if x[0].left:
                    dq.append((x[0].left, x[1] * 2))
                if x[0].right:
                    dq.append((x[0].right, x[1] * 2 + 1))
                sz -= 1

        return res


def test_width_of_binary_tree():
    solution = Solution()
    node3 = TreeNode(3, TreeNode(5))
    root = TreeNode(1, node3, TreeNode(2))
    assert solution.widthOfBinaryTree(root) == 2, 'wrong result'


if __name__ == '__main__':
    test_width_of_binary_tree()
