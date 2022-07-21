from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # LCA but TLE
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # distance of node1, node2 = distance of node1, root + distance of node2, root - 2 * distance of LCA, root
        def dist(node1, node2):
            node = LCA(root, node1, node2)
            return nodes[node1] + nodes[node2] - 2 * nodes[node]

        def LCA(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root

            left = LCA(root.left, p, q)
            right = LCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        def dfs(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root)

            nodes[root] = depth
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        leaves = list()
        nodes = defaultdict(int)
        dfs(root, 0)

        res = 0
        for node1 in leaves:
            for node2 in leaves:
                if node1 != node2 and dist(node1, node2) <= distance:
                    res += 1
        return res // 2


def test_count_pairs():
    solution = Solution()
    assert solution.countPairs(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)), 3) == 1, 'wrong result'
    assert solution.countPairs(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))), 3) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_pairs()

