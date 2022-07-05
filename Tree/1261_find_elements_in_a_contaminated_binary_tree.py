from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.tree = set()
        self.preorder(root, -1, False)
        pass

    def preorder(self, root: Optional[TreeNode], parent: int, is_left: bool):
        if not root:
            return

        if parent == -1:
            val = 0
        elif is_left:
            val = parent * 2 + 1
        else:
            val = parent * 2 + 2

        self.tree.add(val)
        if root.left:
            self.preorder(root.left, val, True)
        if root.right:
            self.preorder(root.right, val, False)

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
