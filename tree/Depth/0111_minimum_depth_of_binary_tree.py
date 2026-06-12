from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        dq = deque([root])
        res = 0
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                res += 1
                if node.left == node.right:
                    return res
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return res

    def minDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)

        return max(left_min, right_min) + 1 if min(left_min, right_min) == 0 else min(left_min, right_min) + 1


def test_min_depth():
    solution = Solution()
    assert solution.minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 2, 'wrong result'
    assert solution.minDepth(TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))) == 5, 'wrong result'


if __name__ == '__main__':
    test_min_depth()
