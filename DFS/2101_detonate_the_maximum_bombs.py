from typing import List


class Solution:
    # dfs
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        res = 0
        g = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    g[i].append(j)

        def dfs(node, seen):
            for child in g[node]:
                if child not in seen:
                    seen.add(child)
                    dfs(child, seen)

        for i in range(n):
            seen = {i}
            dfs(i, seen)
            res = max(res, len(seen))

        return res

    # bfs
    def maximumDetonation1(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                dis = (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2
                if dis <= bombs[i][2] ** 2:
                    g[i].append(j)
                if dis <= bombs[j][2] ** 2:
                    g[j].append(i)

        res = 0
        for i in range(n):
            seen = {i}
            cur = 1
            q = [i]
            while q:
                u = q.pop()
                for v in g[u]:
                    if v not in seen:
                        seen.add(v)
                        cur += 1
                        q.append(v)
            res = max(res, cur)

        return res


def test_maximum_detonation():
    solution = Solution()
    assert solution.maximumDetonation([[2, 1, 3], [6, 1, 4]]) == 2, 'wrong result'
    assert solution.maximumDetonation([[1, 1, 5], [10, 10, 5]]) == 1, 'wrong result'
    assert solution.maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]) == 5, 'wrong result'


if __name__ == '__main__':
    test_maximum_detonation()
