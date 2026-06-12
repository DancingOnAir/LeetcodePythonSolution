from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = list()

        def helper(root, is_root):
            if not root:
                return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root

        helper(root, True)
        return res

    def delNodes1(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        stk = list()
        res = list()
        if root.val in to_delete:
            stk.extend([root.left, root.right])
        stk = [(root, None, 0)]
        while stk:
            node, pre, left = stk.pop()
            if node.left:
                if node.val in to_delete:
                    stk.append((node.left, None, True))
                else:
                    stk.append((node.left, node, True))
            if node.right:
                if node.val in to_delete:
                    stk.append((node.right, None, False))
                else:
                    stk.append((node.right, node, False))

            if pre:
                if node.val in to_delete:
                    if left:
                        pre.left = None
                    else:
                        pre.right = None
            else:
                if node.val not in to_delete:
                    res.append(node)
        return res


def test_del_nodes():
    solution = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    res = solution.delNodes(root, [3, 5])

    assert len(res) == 3, 'wrong result'
    assert res[0].val == 1, 'wrong result'
    assert res[0].left.val == 2, 'wrong result'
    assert res[0].left.left.val == 4, 'wrong result'
    assert res[1].val == 6, 'wrong result'
    assert res[2].val == 7, 'wrong result'


if __name__ == '__main__':
    test_del_nodes()

