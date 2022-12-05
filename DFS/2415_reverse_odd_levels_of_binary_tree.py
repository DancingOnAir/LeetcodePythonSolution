from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2, is_odd_level):
            if not node1:
                return
            if is_odd_level:
                node1.val, node2.val = node2.val, node1.val
            # 这里node1一直left就是前序遍历，node2一直right，就是后序遍历，比较树里以中心线对称的2个结点，如果符合条件就交换值，参考q101
            dfs(node1.left, node2.right, not is_odd_level)
            # 同理，node1是后续遍历，node2是前序遍历
            dfs(node2.left, node1.right, not is_odd_level)
        dfs(root.left, root.right, True)
        return root


def test_reverse_odd_levels():
    solution = Solution()
    # assert solution.reverseOddLevels(
        # TreeNode(2, TreeNode(5, TreeNode(8), TreeNode(13)), TreeNode(3, TreeNode(21), TreeNode(34)))) == [2, 5, 3, 8, 13, 21, 34], 'wrong result'
    root = solution.reverseOddLevels(TreeNode(7, TreeNode(13), TreeNode(11)))
    assert root.val == 7, 'wrong result'
    assert root.left.val == 11, 'wrong result'
    assert root.right.val == 13, 'wrong result'


if __name__ == '__main__':
    test_reverse_odd_levels()
