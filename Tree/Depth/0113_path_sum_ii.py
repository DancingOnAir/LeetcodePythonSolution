from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def help(node, x, nums):
            if not node:
                return
            if not node.left and not node.right and node.val == x:
                nonlocal res
                res.append(nums + [x])
                return

            help(node.left, x - node.val, nums + [node.val])
            help(node.right, x - node.val, nums + [node.val])

        res = list()
        help(root, targetSum, [])
        return res


def test_path_sum():
    solution = Solution()
    assert solution.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22) == [[5,4,11,2],[5,8,4,5]], 'wrong result'
    assert solution.pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5) == [], 'wrong result'
    assert solution.pathSum(TreeNode(1, TreeNode(2)), 0) == [], 'wrong result'


if __name__ == '__main__':
    test_path_sum()
