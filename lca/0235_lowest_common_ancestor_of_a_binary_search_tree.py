# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # recursive template
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root

        left, right = (self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right))
        return root if left and right else left or right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


def test_lowest_common_ancestor():
    node_list = [TreeNode(x) for x in range(10)]
    node_list[6].left = node_list[2]
    node_list[6].right = node_list[8]
    node_list[2].left = node_list[0]
    node_list[2].right = node_list[4]
    node_list[8].left = node_list[7]
    node_list[8].right = node_list[9]
    node_list[4].left = node_list[3]
    node_list[4].right = node_list[5]

    solution = Solution()
    assert solution.lowestCommonAncestor(node_list[6], node_list[2], node_list[8]) == node_list[6], 'wrong result'
    assert solution.lowestCommonAncestor(node_list[6], node_list[2], node_list[4]) == node_list[2], 'wrong result'


if __name__ == '__main__':
    test_lowest_common_ancestor()
