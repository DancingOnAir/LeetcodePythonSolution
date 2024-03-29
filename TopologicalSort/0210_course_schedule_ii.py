from typing import List
from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = defaultdict(int)
        graph = defaultdict(list)
        for u, v in prerequisites:
            in_degrees[u] += 1
            graph[v].append(u)

        res = list()
        q = set(range(numCourses)) - set(in_degrees)
        while q:
            u = q.pop()
            res.append(u)
            for v in graph[u]:
                in_degrees[v] -= 1
                in_degrees[v] or q.add(v)

        return res * (len(res) == numCourses)

    def findOrder1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            in_degrees[u] += 1

        res = list()
        dq = deque(i for i, val in enumerate(in_degrees) if val == 0)
        while dq:
            u = dq.popleft()
            res.append(u)
            for v in graph[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    dq.append(v)
        return res if len(res) == numCourses else []


def test_find_order():
    solution = Solution()
    assert solution.findOrder(2, [[1, 0]]) == [0, 1], 'wrong result'
    assert solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 2, 1, 3], 'wrong result'


if __name__ == '__main__':
    test_find_order()
