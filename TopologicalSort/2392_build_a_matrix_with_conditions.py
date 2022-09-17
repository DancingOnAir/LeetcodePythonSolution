from typing import List
from collections import defaultdict, deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # 拓扑排序，创建2个队列，1个dq放入度为0的点，res放排序好的点。
        def topological_sort(edges: List[List[int]]) -> List[int]:
            graph = [[] for _ in range(k)]
            in_degree = [0] * k
            for u, v in edges:
                graph[u - 1].append(v - 1)
                in_degree[v - 1] += 1
            # find the node which in degree is 0
            dq = deque(i for i, val in enumerate(in_degree) if val == 0)
            res = list()
            while dq:
                u = dq.popleft()
                res.append(u)
                for v in graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        dq.append(v)
            return res if len(res) == k else None

        row = topological_sort(rowConditions)
        col = topological_sort(colConditions)
        if row is None or col is None:
            return []

        res = [[0] * k for _ in range(k)]
        pos = {val: i for i, val in enumerate(col)}
        for i, val in enumerate(row):
            res[i][pos[val]] = val + 1
        return res


def test_build_matrix():
    solution = Solution()


if __name__ == '__main__':
    test_build_matrix()
