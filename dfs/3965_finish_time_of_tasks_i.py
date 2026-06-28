class Solution:
    def finishTime(self, n: int, edges: list[list[int]], baseTime: list[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)

        def dfs(u: int) -> int:
            if not g[u]:
                return baseTime[u]
            earliest = float('inf')
            latest = 0
            for v in g[u]:
                t = dfs(v)
                earliest = min(earliest, t)
                latest = max(latest, t)
            return latest * 2 - earliest + baseTime[u]
        return dfs(0)


def test_finish_time():
    solution = Solution()
    assert solution.finishTime(3, edges = [[0,1],[1,2]], baseTime = [9,5,3]) == 17, 'wrong result'
    assert solution.finishTime(3, edges = [[0,1],[0,2]], baseTime = [4,7,6]) == 12, 'wrong result'
    assert solution.finishTime(4, edges = [[0,1],[0,2],[2,3]], baseTime = [5,8,2,1]) == 18, 'wrong result'


if __name__ == '__main__':
    test_finish_time()

