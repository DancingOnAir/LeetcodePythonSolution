from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if not node:
                return

            nonlocal res
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        res = list()
        dfs(root, 0)
        return res


def test_right_side_view():
    solution = Solution()
    assert solution.rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))) == [1, 3, 4], 'wrong result'
    assert solution.rightSideView(TreeNode(1, None, TreeNode(3))) == [1, 3], 'wrong result'
    assert solution.rightSideView(None) == [], 'wrong result'


if __name__ == '__main__':
    test_right_side_view()
