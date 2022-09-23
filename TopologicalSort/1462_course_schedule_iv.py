from typing import List
from collections import defaultdict, deque


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        pres = [set() for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)
            in_degree[v] += 1
            pres[v].add(u)

        dq = deque(i for i, val in enumerate(in_degree) if val == 0)
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                pres[v] |= pres[u]
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    dq.append(v)
        return [u in pres[v] for u, v in queries]


def test_check_if_prerequisite():
    solution = Solution()
    assert solution.checkIfPrerequisite(5, [[0,1],[1,2],[2,3],[3,4]], [[0,4],[4,0],[1,3],[3,0]]) == [True,False,True,False], 'wrong result'
    assert solution.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True], 'wrong result'
    assert solution.checkIfPrerequisite(2, [], [[1, 0], [0, 1]]) == [False, False], 'wrong result'
    assert solution.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]) == [True, True], 'wrong result'


if __name__ == '__main__':
    test_check_if_prerequisite()
