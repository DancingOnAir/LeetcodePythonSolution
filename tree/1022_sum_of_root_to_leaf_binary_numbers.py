from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], val=0) -> int:
        if not root:
            return 0
        val = val * 2 + root.val
        if root.left == root.right:
            return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)

    # filter(function, iterable)
    #  If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
    def sumRootToLeaf2(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node.left and not node.right:
                self.res += node.val
            for child in filter(None, [node.left, node.right]):
                child.val += node.val * 2
                dfs(child)

        self.res = 0
        dfs(root)
        return self.res

    # recursive
    def sumRootToLeaf1(self, root: Optional[TreeNode]) -> int:
        def preorder(node, cur):
            cur.append(str(node.val))
            if not node.left and not node.right:
                self.res += int(''.join(cur), 2)
                return
            if node.left:
                preorder(node.left, cur)
                cur.pop()
            if node.right:
                preorder(node.right, cur)
                cur.pop()

        self.res = 0
        preorder(root, [])
        return self.res


def test_sum_root_to_leaf():
    solution = Solution()
    assert solution.sumRootToLeaf(TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))) == 22, 'wrong result'
    assert solution.sumRootToLeaf(TreeNode(0, TreeNode(1, TreeNode(0)), TreeNode(0, TreeNode(0, None, TreeNode(1, None, TreeNode(1))), TreeNode(0)))) == 5, 'wrong result'


if __name__ == '__main__':
    test_sum_root_to_leaf()

