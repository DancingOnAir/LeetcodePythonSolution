from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def postorder(node):
            if not node:
                return []

            left = postorder(node.left)
            right = postorder(node.right)

            res = list()
            if not left and not right:
                return [chr(node.val + ord('a'))]

            for ch in left:
                res.append(ch + chr(node.val + ord('a')))
            for ch in right:
                res.append(ch + chr(node.val + ord('a')))
            return res

        letters = sorted(postorder(root))
        return letters[0]

    # dfs + backtrack
    def smallestFromLeaf1(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if not root:
                return

            if root.left is None and root.right is None:
                self.cur.append(chr(root.val + ord('a')))
                self.m.append(''.join(self.cur[::-1]))
                self.cur.pop()
                return

            self.cur.append(chr(root.val + ord('a')))
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            self.cur.pop()

        self.m = list()
        self.cur = list()
        dfs(root)
        return min(self.m)


def test_smallest_from_leaf():
    solution = Solution()
    assert solution.smallestFromLeaf(TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))) == 'dba', 'wrong result'
    assert solution.smallestFromLeaf(TreeNode(25, TreeNode(1, TreeNode(1), TreeNode(3)), TreeNode(3, TreeNode(0), TreeNode(2)))) == 'adz', 'wrong result'
    assert solution.smallestFromLeaf(TreeNode(2, TreeNode(2, None, TreeNode(1, TreeNode(0))), TreeNode(1, TreeNode(0)))) == 'abc', 'wrong result'


if __name__ == '__main__':
    test_smallest_from_leaf()
