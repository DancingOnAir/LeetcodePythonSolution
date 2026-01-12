from typing import List
from heapq import heappop, heappush, heapify
from collections import defaultdict


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.hp = []
        self.m = defaultdict(list)
        for u, t, p in tasks:
            self.hp.append([-p, -t, u])
            self.m[t] = [p, u]
        heapify(self.hp)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.m[taskId] = [priority, userId]
        heappush(self.hp, [-priority, -taskId, userId])

    # 懒修改
    def edit(self, taskId: int, newPriority: int) -> None:
        self.add(self.m[taskId][1], taskId, newPriority)

    # 懒删除
    def rmv(self, taskId: int) -> None:
        self.m[taskId] = [-1, -1]

    def execTop(self) -> int:
        while self.hp:
            p, t, u = heappop(self.hp)
            if self.m[-t] == [-p, u]:
                self.rmv(-t)
                return u
        return -1


def test_task_manager():
    obj = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
    obj.add(4, 104, 5)
    obj.edit(102, 8)
    assert obj.execTop() == 3, 'wrong result'
    obj.rmv(101)
    obj.add(5, 105, 15)
    assert obj.execTop() == 5, 'wrong result'


if __name__ == '__main__':
    test_task_manager()
