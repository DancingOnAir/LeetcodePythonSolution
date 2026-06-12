from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # level order
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = 0
        dq = deque([root])
        while dq:
            res += 1
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res

    # recursive
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return max(left_max, right_max) + 1


def test_max_depth():
    solution = Solution()
    assert solution.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 3, 'wrong result'
    assert solution.maxDepth(TreeNode(1, None, TreeNode(2))) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_depth()
