from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = list()
        dq = deque([root])
        even = True

        while dq:
            vals = list()
            for _ in range(len(dq)):
                node = dq.popleft()
                vals.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(vals if even else vals[::-1])
            even = not even

        return res


def test_zigzag_level_order():
    solution = Solution()
    assert solution.zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == [[3],[20,9],[15,7]], 'wrong result'
    assert solution.zigzagLevelOrder(TreeNode(1)) == [[1]], 'wrong result'
    assert solution.zigzagLevelOrder(None) == [], 'wrong result'


if __name__ == '__main__':
    test_zigzag_level_order()
