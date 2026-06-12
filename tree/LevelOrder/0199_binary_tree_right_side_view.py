from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        dq = deque([root])
        res = list()
        depth = 0
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if len(res) == depth:
                    res.append(node.val)

                if node.right:
                    dq.append(node.right)
                if node.left:
                    dq.append(node.left)
            depth += 1
        return res


def test_right_side_view():
    solution = Solution()
    assert solution.rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))) == [1, 3, 4], 'wrong result'
    assert solution.rightSideView(TreeNode(1, None, TreeNode(3))) == [1, 3], 'wrong result'
    assert solution.rightSideView(None) == [], 'wrong result'


if __name__ == '__main__':
    test_right_side_view()