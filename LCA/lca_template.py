from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# pythonic version
def find_least_common_ancestor_recursive_pythonic(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    if root in (None, p, q):
        return root

    left, right = (find_least_common_ancestor_recursive_pythonic(child, p, q) for child in (root.left, root.right))
    return root if left and right else left or right


def find_least_common_recursive_ancestor(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    if root == p or root == q:
        return root

    left = find_least_common_recursive_ancestor(root.left, p, q)
    right = find_least_common_recursive_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


def find_least_common_dfs_ancestor(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(r, c, depth):
        parents[r] = c
        depths[r] = depth

        dfs(r.left, r, depth+1)
        dfs(r.right, r, depth+1)

    def jump_parent(r, steps):
        while steps > 0:
            r = parents[r]
            steps -= 1
        return r

    parents = dict()
    depths = dict()

    dfs(root, None, 0)
    if depths[q] > depths[p]:
        q = jump_parent(q, depths[q] - depths[p])
    else:
        p = jump_parent(p, depths[p] - depths[q])

    while p != q:
        q = parents[q]
        p = parents[p]

    return q
