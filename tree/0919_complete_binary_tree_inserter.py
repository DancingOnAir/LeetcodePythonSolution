from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.tree = [root]
        for node in self.tree:
            if node.left:
                self.tree.append(node.left)
            if node.right:
                self.tree.append(node.right)

    def insert(self, val: int) -> int:
        n = len(self.tree)
        self.tree.append(TreeNode(val))
        if n & 1:
            self.tree[(n - 1) // 2].left = self.tree[-1]
        else:
            self.tree[(n - 1) // 2].right = self.tree[-1]
        return self.tree[(n - 1) // 2].val

    def get_root(self) -> Optional[TreeNode]:
        return self.tree[0]


# bfs
class CBTInserter1:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.nxt = None
        self.dq = deque([root])
        while self.dq:
            cur = self.dq[0]
            if cur.left and cur.right:
                self.dq.append(cur.left)
                self.dq.append(cur.right)
                self.dq.popleft()
            else:
                if cur.left:
                    self.dq.append(cur.left)
                self.nxt = cur
                break

    def insert(self, val: int) -> int:
        res = self.nxt.val
        if not self.nxt.left:
            self.nxt.left = TreeNode(val)
            self.dq.append(self.nxt.left)
        else:
            self.nxt.right = TreeNode(val)
            self.dq.append(self.nxt.right)
            self.dq.popleft()
            self.nxt = self.dq[0]

        return res

    def get_root(self) -> Optional[TreeNode]:
        return self.root


def test_cbt_intserter():
    root = TreeNode(1, TreeNode(2))
    obj = CBTInserter(root)
    assert obj.insert(3) == 1, 'wrong result'
    assert obj.insert(4) == 2, 'wrong result'
    assert obj.get_root().val == 1, 'wrong result'
    assert obj.get_root().left.val == 2, 'wrong result'
    assert obj.get_root().right.val == 3, 'wrong result'
    assert obj.get_root().left.left.val == 4, 'wrong result'


if __name__ == '__main__':
    test_cbt_intserter()
