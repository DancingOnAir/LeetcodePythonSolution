from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # top-down
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, l, r):
            if not node:
                return
            nonlocal res
            res = max(res, l, r)
            dfs(node.left, 0, l + 1)
            dfs(node.right, r + 1, 0)

        res = 0
        dfs(root, 0, 0)
        return res

    def longestZigZag1(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left, sz):
            if not node:
                return

            nonlocal res
            res = max(res, sz)

            if is_left:
                dfs(node.left, True, 1)
                dfs(node.right, False, sz + 1)
            else:
                dfs(node.left, True, sz + 1)
                dfs(node.right, False, 1)

        res = 0
        dfs(root, True, 0)
        dfs(root, False, 0)
        return res


def test_longest_zigzag():
    solution = Solution()
    assert solution.longestZigZag(TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1))))) == 3, 'wrong result'
    assert solution.longestZigZag(TreeNode(1, TreeNode(1, None, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1))), TreeNode(1))) == 4, 'wrong result'
    assert solution.longestZigZag(TreeNode(1)) == 0, 'wrong result'


if __name__ == '__main__':
    test_longest_zigzag()
