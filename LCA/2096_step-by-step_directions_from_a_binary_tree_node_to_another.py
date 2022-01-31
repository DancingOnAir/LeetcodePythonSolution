from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pass


def test_get_directions():
    solution = Solution()

    node_list = [TreeNode(x) for x in range(7)]
    node_list[5].left = node_list[1]
    node_list[5].right = node_list[2]
    node_list[1].left = node_list[3]
    node_list[2].left = node_list[6]
    node_list[2].right = node_list[4]
    assert solution.getDirections(node_list[5], 3, 6) == "UURL", 'wrong result'

    node_list = [TreeNode(x) for x in range(3)]
    node_list[2].left = node_list[1]

    assert solution.getDirections(node_list[5], 2, 1) == "L", 'wrong result'