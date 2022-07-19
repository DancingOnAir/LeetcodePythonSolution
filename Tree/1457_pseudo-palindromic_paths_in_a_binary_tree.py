from typing import Optional
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode], count: int = 0) -> int:
        if not root:
            return 0

        count ^= 1 << (root.val - 1)
        res = self.pseudoPalindromicPaths(root.left, count) + self.pseudoPalindromicPaths(root.right, count)
        if root.left == root.right:
            # i & (i - 1): 二进制下的最右边的1置为0
            # 拓展：(i > 0 && ((i & (i - 1)) == 0)是判断i是不是2的次幂
            if count & (count - 1) == 0:
                res += 1
        return res

    # TLE
    def pseudoPalindromicPaths1(self, root: Optional[TreeNode]) -> int:
        def preorder(node, path):
            if node:
                path.append(node.val)
                if not node.left and not node.right:
                    if sum(1 for x in Counter(path).values() if x & 1) <= 1:
                        self.res += 1

                preorder(node.left, path)
                preorder(node.right, path)
                path.pop()

        self.res = 0
        preorder(root, [])
        return self.res


def test_pseudo_palindromic_paths():
    solution = Solution()
    assert solution.pseudoPalindromicPaths(TreeNode(3, TreeNode(8), TreeNode(5, TreeNode(5, None, TreeNode(8,
                                                                                                           TreeNode(8,
                                                                                                                    TreeNode(
                                                                                                                        2,
                                                                                                                        None,
                                                                                                                        TreeNode(
                                                                                                                            1))))),
                                                                             TreeNode(6, None, TreeNode(
                                                                                 5))))) == 0, 'wrong result'
    assert solution.pseudoPalindromicPaths(
        TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))) == 2, 'wrong result'
    assert solution.pseudoPalindromicPaths(
        TreeNode(2, TreeNode(1, TreeNode(1), TreeNode(3, None, TreeNode(1))), TreeNode(1))) == 1, 'wrong result'


if __name__ == '__main__':
    test_pseudo_palindromic_paths()
