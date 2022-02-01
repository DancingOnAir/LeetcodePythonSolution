# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right


def test_lowest_common_ancestor():
    node_list = [TreeNode(x) for x in range(9)]
    node_list[3].left = node_list[5]
    node_list[3].right = node_list[1]
    node_list[5].left = node_list[6]
    node_list[5].right = node_list[2]
    node_list[2].left = node_list[7]
    node_list[2].right = node_list[4]
    node_list[1].left = node_list[0]
    node_list[1].right = node_list[8]

    solution = Solution()
    assert solution.lowestCommonAncestor(node_list[3], node_list[5], node_list[1]) == node_list[3], 'wrong result'
    assert solution.lowestCommonAncestor(node_list[3], node_list[5], node_list[4]) == node_list[5], 'wrong result'


if __name__ == '__main__':
    test_lowest_common_ancestor()
