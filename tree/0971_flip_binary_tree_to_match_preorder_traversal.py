from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # stack
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        res = list()
        stk = [root]
        idx = 0

        while stk:
            node = stk.pop()
            if not node:
                continue
            if node.val != voyage[idx]:
                return [-1]

            idx += 1
            if node.right and node.right.val == voyage[idx]:
                if node.left:
                    res.append(node.val)
                stk.extend([node.left, node.right])
            else:
                stk.extend([node.right, node.left])

        return res

    # preorder
    def flipMatchVoyage2(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        def preorder(root):
            if not root or self.idx >= len(voyage):
                return
            if root.val != voyage[self.idx]:
                self.res.append(None)
                return

            flag = 1
            self.idx += 1

            if root.left and root.left.val != voyage[self.idx]:
                self.res.append(root.val)
                flag = -1

            for node in [root.left, root.right][::flag]:
                preorder(node)

        self.res = list()
        self.idx = 0
        preorder(root)
        return [-1] if None in self.res else self.res


def test_flip_match_voyage():
    solution = Solution()
    assert solution.flipMatchVoyage(TreeNode(1, TreeNode(2)), [2, 1]) == [-1]
    assert solution.flipMatchVoyage(TreeNode(1, TreeNode(2), TreeNode(3)), [1, 3, 2]) == [1]
    assert solution.flipMatchVoyage(TreeNode(1, TreeNode(2), TreeNode(3)), [1, 2, 3]) == []


if __name__ == '__main__':
    test_flip_match_voyage()
