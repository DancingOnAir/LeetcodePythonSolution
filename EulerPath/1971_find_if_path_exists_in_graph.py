from typing import List


class Solution:
    # euler path
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u):
            if u == destination:
                return True
            res = False
            while g[u]:
                res |= dfs(g[u].pop())
            return res
        return dfs(source)

    # iterative
    def validPath2(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        seen = {source}
        stk = [source]
        while stk:
            u = stk.pop()
            for v in g[u]:
                if v == destination:
                    return True
                if v not in seen:
                    seen.add(v)
                    stk.append(v)
        return destination in seen

    # recursive
    def validPath1(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(u, g, seen):
            if u == destination:
                return True

            if u not in seen:
                seen.add(u)
                for v in g[u]:
                    if dfs(v, g, seen):
                        return True
                return False

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        seen = set()
        return dfs(source, g, seen)


def test_valid_path():
    solution = Solution()
    assert solution.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2), 'wrong result'
    assert not solution.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5), 'wrong result'


if __name__ == '__main__':
    test_valid_path()
