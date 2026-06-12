from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def bfs(root: Optional[TreeNode]):
            if root.val in m:
                return True
            m.add(k - root.val)
            if root.left and bfs(root.left):
                return True
            if root.right and bfs(root.right):
                return True
            return False
        m = set()
        return bfs(root)


def test_find_target():
    solution = Solution()

    node3 = TreeNode(3, TreeNode(2), TreeNode(4))
    node6 = TreeNode(6, None, TreeNode(7))
    root = TreeNode(5, node3, node6)
    assert solution.findTarget(root, 9), 'wrong result'


if __name__ == '__main__':
    test_find_target()
