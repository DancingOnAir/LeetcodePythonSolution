from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return True, 0, float('inf'), float('-inf')

            nonlocal res
            bst1, s1, min1, max1 = dfs(node.left)
            bst2, s2, min2, max2 = dfs(node.right)
            if bst1 and bst2 and max1 < node.val < min2:
                v = node.val + s1 + s2
                res = max(res, v)
                return True, v, min(min1, node.val), max(max2, node.val)

            return False, 0, float('inf'), float('-inf')

        res = 0
        dfs(root)
        return res

    def maxSumBST1(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return True, None, None, None
            left_is_bst, left_node, left_min_val, left_max_val = dfs(node.left)
            right_is_bst, right_node, right_min_val, right_max_val = dfs(node.right)

            if left_is_bst and right_is_bst:
                node_val = node.val
                if not left_node and not right_node:
                    self.res = max(self.res, node.val)
                    return True, node, node_val, node_val
                elif not right_node and left_max_val < node.val:
                    node.val += left_node.val
                    self.res = max(self.res, node.val)
                    return True, node, left_min_val, node_val
                elif not left_node and right_min_val > node.val:
                    node.val += right_node.val
                    self.res = max(self.res, node.val)
                    return True, node, node_val, right_max_val
                elif left_node and right_node and left_max_val < node.val < right_min_val:
                    node.val += left_node.val + right_node.val
                    self.res = max(self.res, node.val)
                    return True, node, left_min_val, right_max_val

            return False, node, node.val, node.val

        self.res = 0
        dfs(root)
        return self.res


def test_max_sum_bst():
    solution = Solution()

    root1 = TreeNode(1, TreeNode(4, TreeNode(2), TreeNode(4)), TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6))))
    assert solution.maxSumBST(root1) == 20, 'wrong result'

    root2 = TreeNode(4, TreeNode(3, TreeNode(1), TreeNode(2)))
    assert solution.maxSumBST(root2) == 2, 'wrong result'

    root3 = TreeNode(-4, TreeNode(-2), TreeNode(-5))
    assert solution.maxSumBST(root3) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_sum_bst()
