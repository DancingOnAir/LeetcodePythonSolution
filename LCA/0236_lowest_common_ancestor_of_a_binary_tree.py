# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        return root if left and right else left or right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(r, u, depth):
            if r is None:
                return

            parents[r] = u
            depths[r] = depth

            dfs(r.left, r, depth+1)
            dfs(r.right, r, depth+1)

        def jump_parent(r, steps):
            while steps > 0:
                r = parents[r]
                steps -= 1

            return r

        parents = dict()
        depths = dict()

        dfs(root, None, 0)
        if depths[p] < depths[q]:
            q = jump_parent(q, depths[q] - depths[p])
        else:
            p = jump_parent(p, depths[p] - depths[q])

        while p != q:
            p = parents[p]
            q = parents[q]

        return p


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
