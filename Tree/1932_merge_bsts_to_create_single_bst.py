from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        return trees[0]


def test_can_merge():
    solution = Solution()

    res1 = solution.canMerge([TreeNode(2, TreeNode(1)), TreeNode(3, TreeNode(2), TreeNode(5)), TreeNode(5, TreeNode(4))])
    assert res1.val == 3, 'wrong result'
    assert res1.left.val == 2, 'wrong result'
    assert res1.right.val == 5, 'wrong result'

    res2 = solution.canMerge([TreeNode(5, TreeNode(3), TreeNode(8)), TreeNode(3, TreeNode(2), TreeNode(6))])
    assert res2.val == 5, 'wrong result'
    assert res2.left.val == 3, 'wrong result'
    assert res2.right.val == 8, 'wrong result'

    res3 = solution.canMerge([TreeNode(5, TreeNode(4)), TreeNode(3)])
    assert not res3, 'wrong result'


if __name__ == '__main__':
    test_can_merge()
