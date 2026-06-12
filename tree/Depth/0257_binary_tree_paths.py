from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, arr):
            if not node:
                return

            if not node.left and not node.right:
                nonlocal res
                res.append('->'.join(map(str, arr + [node.val])))
                return

            dfs(node.left, arr + [node.val])
            dfs(node.right, arr + [node.val])

        res = list()
        dfs(root, [])
        return res


def test_binary_tree_paths():
    solution = Solution()
    assert solution.binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))) == ["1->2->5","1->3"], 'wrong result'
    assert solution.binaryTreePaths(TreeNode(1)) == ["1"], 'wrong result'


if __name__ == '__main__':
    test_binary_tree_paths()
