from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        dq = deque()
        dq.append(root)

        pre = root.val
        while len(dq) > 0:
            x = dq.popleft()
            if x.val != pre:
                return False

            if x.left:
                dq.append(x.left)
            if x.right:
                dq.append(x.right)
        return True


def test_is_unival_tree():
    solution = Solution()

    root = TreeNode(1)
    assert solution.isUnivalTree(root), 'wrong result'


if __name__ == '__main__':
    test_is_unival_tree()
