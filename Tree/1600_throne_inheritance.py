from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = list()

    def birth(self, child):
        self.children.append(TreeNode(child))


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = TreeNode(kingName)
        self.death = set()

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
        self.death.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = list()




def test_throne_inheritance():
    obj = ThroneInheritance("king")
    obj.birth("king", "andy")
    obj.birth("king", "bob")
    obj.birth("king", "catherine")
    obj.birth("king", "matthew")
    obj.birth("bob", "alex")
    obj.birth("bob", "asha")

    assert obj.getInheritanceOrder() == ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], 'wrong result'
    obj.death("bob")
    assert obj.getInheritanceOrder() == ["king", "andy", "matthew", "alex", "asha", "catherine"], 'wrong result'


if __name__ == '__main__':
    test_throne_inheritance()
