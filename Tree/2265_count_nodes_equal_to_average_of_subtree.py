from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # return total of subtree, num of nodes
        def postorder(node):
            nonlocal res
            if not node:
                return 0, 0
            if node.left == node.right:
                res += 1
                return node.val, 1

            left_total, left_num = postorder(node.left)
            right_total, right_num = postorder(node.right)
            if node.val == (left_total + right_total + node.val) // (left_num + right_num + 1):
                res += 1
            return left_total + right_total + node.val, left_num + right_num + 1

        res = 0
        postorder(root)
        return res


def test_average_of_subtree():
    solution = Solution()
    assert solution.averageOfSubtree(TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))) == 5, 'wrong result'
    assert solution.averageOfSubtree(TreeNode(1)) == 1, 'wrong result'


if __name__ == '__main__':
    test_average_of_subtree()
