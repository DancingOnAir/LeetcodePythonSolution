class Solution:
    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        def dfs(u: int) -> int:
            tot = score[u]
            if not g[u]:
                return tot
            mn = float('inf')
            for v in g[u]:
                s = dfs(v)
                tot += s
                mn = min(mn, s)
            if mn < 0 or op[u]:
                tot -= mn
            return tot

        return dfs(0)


def test_max_score():
    solution = Solution()
    assert solution.maxScore([-1, 0, 0, 0, 1, 2, 3, 3], op=[1, 1, 0, 0, 1, 1, 0, 1],
                             score=[5, 6, 1, 2, 3, 2, 3, -3]) == 16, 'wrong result'
    assert solution.maxScore([-1, 0, 0], op=[0, 0, 0], score=[1, 2, 3]) == 6, 'wrong result'
    assert solution.maxScore([-1], op=[1], score=[-10]) == -10, 'wrong result'


if __name__ == '__main__':
    test_max_score()
