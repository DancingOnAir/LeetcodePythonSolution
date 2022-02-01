from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# pythonic version
def find_least_common_ancestor_pythonic(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    if root in (None, p, q):
        return root

    left, right = (find_least_common_ancestor_pythonic(child, p, q) for child in (root.left, root.right))
    return root if left and right else left or right


def find_least_common_ancestor(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    if root == p or root == q:
        return root

    left = find_least_common_ancestor(root.left, p, q)
    right = find_least_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right
