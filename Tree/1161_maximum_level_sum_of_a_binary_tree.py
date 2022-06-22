from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = level = 0
        max_sum = float('-inf')
        stk = [root]
        while stk:
            tmp = list()
            cur_sum = 0
            level += 1
            for node in stk:
                cur_sum += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            if cur_sum > max_sum:
                max_sum = cur_sum
                res = level
            stk = tmp
        return res


def test_max_level_sum():
    solution = Solution()
    root1 = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
    assert solution.maxLevelSum(root1) == 2, 'wrong result'
    root2 = TreeNode(989, None, TreeNode(10250, TreeNode(98693), TreeNode(-89388, None, TreeNode(-32127))))
    assert solution.maxLevelSum(root2) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_level_sum()
