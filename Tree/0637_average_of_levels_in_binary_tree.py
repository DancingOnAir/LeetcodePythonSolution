from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dq = deque([root])
        res = list()

        while dq:
            k, total = len(dq), 0
            for i in range(k):
                x = dq.popleft()
                total += x.val

                if x.left:
                    dq.append(x.left)
                if x.right:
                    dq.append(x.right)
            res.append(total / k)

        return res


def test_average_of_levels():
    solution = Solution()
    node20 = TreeNode(20, TreeNode(15), TreeNode(7))
    node9 = TreeNode(9)
    root = TreeNode(3, node9, node20)
    assert solution.averageOfLevels(root) == [3.00000, 14.50000, 11.00000], 'wrong result'


if __name__ == "__main__":
    test_average_of_levels()
