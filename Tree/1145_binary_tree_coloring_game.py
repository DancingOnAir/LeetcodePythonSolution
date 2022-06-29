from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # y的最优策略是放在x邻近的节点上，
    # 计算可能存在的(最多3个)子树分别有多少节点, 选节点数最大的那个子树作为y的起始点.
    # 当选取的那个子树节点数大于剩余所有的节点数那么为true，否则为false.
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def preorder(node):
            if not node:
                return

            if node.val == x:
                self.node_y1 = node.left
                self.node_y2 = node.right
                return

            preorder(node.left)
            preorder(node.right)

        def helper(node):
            if not node:
                return 0

            self.y += 1
            helper(node.left)
            helper(node.right)

        self.node_y1, self.node_y2 = None, None
        self.y = 0
        preorder(root)
        helper(self.node_y1)
        y1 = self.y
        self.y = 0
        helper(self.node_y2)
        y2 = self.y

        y = max(y1, y2, n - y1 - y2 - 1)
        return y > (n - y)


def test_btree_game_winning_move():
    solution = Solution()

    root3 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert solution.btreeGameWinningMove(root3, 5, 1), 'wrong result'

    root1 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6), TreeNode(7)))
    assert solution.btreeGameWinningMove(root1, 11, 3), 'wrong result'

    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert not solution.btreeGameWinningMove(root2, 3, 1), 'wrong result'


if __name__ == '__main__':
    test_btree_game_winning_move()

