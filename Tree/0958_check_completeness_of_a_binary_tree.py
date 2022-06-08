from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        stk = [root]
        flag = False

        while stk:
            tmp = list()
            for node in stk:
                if not node.left:
                    flag = True
                else:
                    if flag:
                        return False
                    tmp.append(node.left)
                if not node.right:
                    flag = True
                else:
                    if flag:
                        return False
                    tmp.append(node.right)
            stk = tmp

        return True


def test_is_complete_tree():
    solution = Solution()

    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    assert solution.isCompleteTree(root1), 'wrong result'

    root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
    assert not solution.isCompleteTree(root2), 'wrong result'


if __name__ == '__main__':
    test_is_complete_tree()
