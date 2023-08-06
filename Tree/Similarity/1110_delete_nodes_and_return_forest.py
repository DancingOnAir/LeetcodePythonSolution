from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = list()
        s = set(to_delete)

        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in s:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None

            return node
        # decide whether root should be put into the res
        if dfs(root):
            res.append(root)
        return res


def test_del_nodes():
    solution = Solution()
    assert len(solution.delNodes(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4)), [3])) == 1, 'wrong result'
    assert solution.delNodes(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4)), [3])[0].left.right is None, 'wrong result'


if __name__ == '__main__':
    test_del_nodes()
