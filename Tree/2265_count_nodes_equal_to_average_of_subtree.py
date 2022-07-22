from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # node, (total of nodes in subtree, num of nodes in subtree)
        m = {None: (0, 0)}
        res = 0
        pre, node, stk = None, root, list()
        while node or stk:
            if node:
                stk.append(node)
                node = node.left
            else:
                node = stk[-1]
                if node.right and node.right != pre:
                    node = node.right
                else:
                    stk.pop()
                    ls, lc = m[node.left]
                    rs, rc = m[node.right]
                    s, c = ls + rs + node.val, lc + rc + 1
                    m[node] = (s, c)
                    if s // c == node.val:
                        res += 1
                    pre = node
                    node = None

        return res

    # recursive
    def averageOfSubtree1(self, root: Optional[TreeNode]) -> int:
        # return total of nodes' value in subtree, num of nodes, answer of current tree
        def postorder(node):
            # nonlocal res
            if not node:
                return 0, 0, 0

            left_total, left_num, left_res = postorder(node.left)
            right_total, right_num, right_res = postorder(node.right)
            total = left_total + right_total + node.val
            n = left_num + right_num + 1
            # if node.val == total // n:
            #     res += 1
            return total, n, left_res + right_res + (node.val == total // n)
        # res = 0
        return postorder(root)[2]



def test_average_of_subtree():
    solution = Solution()
    assert solution.averageOfSubtree(TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))) == 5, 'wrong result'
    assert solution.averageOfSubtree(TreeNode(1)) == 1, 'wrong result'


if __name__ == '__main__':
    test_average_of_subtree()
