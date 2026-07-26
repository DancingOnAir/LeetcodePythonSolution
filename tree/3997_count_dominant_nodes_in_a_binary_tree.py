class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        def post_order(node: TreeNode) -> int:
            if not node:
                return 0

            mx = max(post_order(node.left), post_order(node.right), node.val)
            if node.val == mx:
                nonlocal res
                res += 1

            return mx

        res = 0
        post_order(root)
        return res


def test_count_dominant_nodes():
    solution = Solution()
    assert solution.countDominantNodes(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(1)))) == 5, 'wrong result'
    assert solution.countDominantNodes(TreeNode(1, TreeNode(2, TreeNode(1), TreeNode(2)), TreeNode(3))) == 4, 'wrong result'


if __name__ == '__main__':
    test_count_dominant_nodes()
