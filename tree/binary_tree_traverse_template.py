from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://blog.csdn.net/qq_24054661/article/details/106928772
    # two stack
    def postorder(self, root: Optional[TreeNode]) -> List[int]:
        stk1 = [root]
        stk2 = []

        while stk1:
            node = stk1.pop()
            stk2.append(node)

            if node.left:
                stk1.append(node.left)
            if node.right:
                stk1.append(node.right)

        res = list()
        while stk2:
            res.append(stk2.pop().val)
        return res


def test():
    solution = Solution()

    assert solution.postorder(TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(5), TreeNode(6)))) == [3, 4, 1, 5, 6, 2, 0], 'wrong result'


if __name__ == '__main__':
    test()
