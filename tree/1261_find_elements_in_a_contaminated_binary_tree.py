from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/discuss/431229/Python-Special-Way-for-find()-without-HashSet-O(1)-Space-O(logn)-Time
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        node = self.root
        for bit in bin(target + 1)[3:]:
            node = node and (node.left, node.right)[int(bit)]
        return bool(node)


class FindElements1:
    def __init__(self, root: Optional[TreeNode]):
        self.tree = set()
        self.preorder(root, 0)

    def preorder(self, root: Optional[TreeNode], idx: int):
        if not root:
            return

        self.tree.add(idx)
        self.preorder(root.left, idx * 2 + 1)
        self.preorder(root.right, idx * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.tree


def test_find_elements():
    root1 = TreeNode(-1, None, TreeNode(-1))
    obj1 = FindElements(root1)
    assert not obj1.find(1), 'wrong result'
    assert obj1.find(2), 'wrong result'

    root2 = TreeNode(-1, TreeNode(-1, TreeNode(-1), TreeNode(-1)), TreeNode(-1))
    obj2 = FindElements(root2)
    assert obj2.find(1), 'wrong result'
    assert obj2.find(3), 'wrong result'
    assert not obj2.find(5), 'wrong result'

    root3 = TreeNode(-1, None, TreeNode(-1, TreeNode(-1, TreeNode(-1))))
    obj3 = FindElements(root3)
    assert obj3.find(2), 'wrong result'
    assert not obj3.find(3), 'wrong result'
    assert not obj3.find(4), 'wrong result'
    assert obj3.find(5), 'wrong result'


if __name__ == '__main__':
    test_find_elements()
