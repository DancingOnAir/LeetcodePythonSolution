from typing import List


class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        # 记录lock[i]的状态，没有lock则为0，否则为对应的user
        self.lock_list = [0] * len(parent)
        self.children = [[] for _ in range(len(parent))]
        # self.tree = {k: [v, 0] for k, v in enumerate(parent)}

    def lock(self, num: int, user: int) -> bool:
        if self.lock_list[num]:
            return False

        self.lock_list[num] = user
        p = self.parent[num]
        while p != -1:
            self.children[p].append(num)
            p = self.parent[p]
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.lock_list[num] != user and user != 0:
            return False
        self.lock_list[num] = 0
        p = self.parent[num]
        while p != -1:
            self.children[p].remove(num)
            p = self.parent[p]
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.lock_list[num]:
            return False
        if not self.children[num]:
            return False

        p = self.parent[num]
        while p != -1:
            if self.lock_list[p]:
                return False
            p = self.parent[p]
        self.lock(num, user)
        for child in self.children[num].copy():
            self.unlock(child, 0)
        return True


def test_locking_tree():
    lockingTree = LockingTree([-1, 0, 0, 1, 1, 2, 2])
    assert lockingTree.lock(2, 2), 'wrong result'
    assert not lockingTree.unlock(2, 3), 'wrong result'
    assert lockingTree.unlock(2, 2), 'wrong result'
    assert lockingTree.lock(4, 5), 'wrong result'
    assert lockingTree.upgrade(0, 1), 'wrong result'
    assert not lockingTree.lock(0, 1), 'wrong result'


if __name__ == '__main__':
    test_locking_tree()

