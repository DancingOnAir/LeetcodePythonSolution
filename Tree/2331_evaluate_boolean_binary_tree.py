from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        stk1 = [root]
        stk2 = list()
        while stk1:
            node = stk1.pop()
            stk2.append(node)

            if node.left:
                stk1.append(node.left)
            if node.right:
                stk1.append(node.right)

        m = dict()
        while stk2:
            node = stk2.pop()
            if node.left == node.right:
                m[node] = node.val
            elif node.val == 2:
                m[node] = m[node.left] or m[node.right]
            else:
                m[node] = m[node.left] and m[node.right]
        return m[root]

    # recursive
    def evaluateTree1(self, root: Optional[TreeNode]) -> bool:
        if root.left == root.right:
            return root.val == 1

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)


def test_evaluate_tree():
    solution = Solution()
    # [3, 2, 3, 2, 2, 3, 2, 1, 1, 2, 3, 0, 1, 0, 3, null, null, null, null, 0, 2, 3, 2, null, null, null, null, null,
    #  null, 0, 0, null, null, 1, 1, 0, 0, 1, 3, null, null, null, null, null, null, null, null, null, null, null, null,
    #  null, null, 3, 0, 1, 1, null, null, null, null, null, null]
    assert not solution.evaluateTree(TreeNode(3, TreeNode(2, TreeNode(2, TreeNode(1), TreeNode(1)), TreeNode(2, TreeNode(2, TreeNode(0), TreeNode(2, TreeNode(1), TreeNode(1))), TreeNode(3, TreeNode(3, TreeNode(0), TreeNode(0)), TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(3, TreeNode(1), TreeNode(1)), TreeNode(0)))))), TreeNode(3, TreeNode(3, TreeNode(0), TreeNode(1)), TreeNode(2, TreeNode(0), TreeNode(3, TreeNode(0), TreeNode(0)))))), 'wrong result'
    assert solution.evaluateTree(TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))), 'wrong result'
    assert solution.evaluateTree(TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))), 'wrong result'
    assert not solution.evaluateTree(TreeNode(0)), 'wrong result'


if __name__ == '__main__':
    test_evaluate_tree()
