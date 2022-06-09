from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs
    # which is pow of 2 minus 1.
    # And for x = 2^k -1, x has a property that x & (x+1) == 0.
    # For a complete tree, it must satisfy at least one of the following condition:
    # if left subtree is a full tree with l nodes,
    # right subtree must have r nodes that l / 2 <= r <= l
    # if right subtree is a full tree with r nodes,
    # left subtree must have l nodes that r <= l <= r * 2 + 1.
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if l & (l + 1) == 0 and l // 2 <= r <= l:
                return l + r + 1
            if r & (r + 1) == 0 and r <= l <= 2 * r + 1:
                return l + r + 1
            return -1
        return dfs(root) > 0

    # pythonic & gracious bfs solution
    def isCompleteTree2(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])

    def isCompleteTree1(self, root: Optional[TreeNode]) -> bool:
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
