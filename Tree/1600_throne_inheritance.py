from typing import List
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = list()

    def birth(self, child):
        self.children.append(TreeNode(child))


class ThroneInheritance1:
    def __init__(self, kingName: str):
        self.root = TreeNode(kingName)
        self.m = set()

    def birth(self, parentName: str, childName: str) -> None:
        dq = deque([self.root])
        while len(dq) > 0:
            x = dq.popleft()
            if x.val == parentName:
                x.birth(childName)
                break

            for child in x.children:
                dq.append(child)

    def death(self, name: str) -> None:
        self.m.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = list()
        dq = deque([self.root])
        while len(dq) > 0:
            x = dq.popleft()
            if x.val not in self.m:
                res.append(x.val)
            for child in reversed(x.children):
                dq.appendleft(child)
        return res


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.nation = defaultdict(list)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.nation[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(cur):
            if cur not in self.dead:
                res.append(cur)
            for child in self.nation[cur]:
                dfs(child)

        res = list()
        dfs(self.king)
        return res


def test_throne_inheritance():
    obj = ThroneInheritance("king")
    obj.birth("king", "andy")
    obj.birth("king", "bob")
    obj.birth("king", "catherine")
    obj.birth("andy", "matthew")
    obj.birth("bob", "alex")
    obj.birth("bob", "asha")

    assert obj.getInheritanceOrder() == ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], 'wrong result'
    obj.death("bob")
    assert obj.getInheritanceOrder() == ["king", "andy", "matthew", "alex", "asha", "catherine"], 'wrong result'


if __name__ == '__main__':
    test_throne_inheritance()
