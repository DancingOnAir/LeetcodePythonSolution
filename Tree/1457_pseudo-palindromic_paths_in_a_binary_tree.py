from typing import Optional
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def preorder(node, path):
            if not node:
                if sum(1 for x in Counter(path).values() if x & 1) == 1:
                    self.res += 1
                return

            path.append(node.val)
            preorder(node.left, path)
            preorder(node.right, path)
            path.pop()

        self.res = 0
        preorder(root, [])
        return self.res


def test_pseudo_palindromic_paths():
    solution = Solution()
    assert solution.pseudoPalindromicPaths(TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))) == 2, 'wrong result'
    assert solution.pseudoPalindromicPaths(TreeNode(2, TreeNode(1, TreeNode(1), TreeNode(3, None, TreeNode(1))), TreeNode(1))) == 1, 'wrong result'


if __name__ == '__main__':
    test_pseudo_palindromic_paths()
