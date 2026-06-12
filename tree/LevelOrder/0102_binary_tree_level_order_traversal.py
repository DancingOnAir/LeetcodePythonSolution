from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = list()
        if root is None:
            return res

        dq = deque([root])
        while dq:
            cur = list()
            for _ in range(len(dq)):
                node = dq.popleft()
                cur.append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(cur)
        return res


def test_level_order():
    solution = Solution()
    assert solution.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == [[3],[9,20],[15,7]], 'wrong result'
    assert solution.levelOrder(TreeNode(1)) == [[1]], 'wrong result'
    assert solution.levelOrder(None) == [], 'wrong result'


if __name__ == '__main__':
    test_level_order()
