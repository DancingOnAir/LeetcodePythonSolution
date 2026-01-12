# https://www.luogu.com.cn/problem/P1352a
class Solution:
    # dfs
    def noSuperiorBall(self, n, happiness, edges):
        g = [[] for _ in range(n)]
        superior = set()
        subordinate = set()
        for u, v in edges:
            superior.add(v - 1)
            subordinate.add(u - 1)
            g[v - 1].append(u - 1)

        for x in (superior - subordinate):
            root = x

        def dfs(u):
            if not g[u]:
                return happiness[u], 0
            select, unselect = happiness[u], 0
            for v in g[u]:
                cur = dfs(v)
                select += cur[1]
                unselect += max(cur)
            return select, unselect

        res = dfs(root)
        return max(res)


def test_no_superior_ball():
    solution = Solution()
    assert solution.noSuperiorBall(7, [1, 1, 1, 1, 1, 1, 1],
                                   [[1, 3], [2, 3], [6, 4], [7, 4], [4, 5], [3, 5]]) == 5, 'wrong result'


if __name__ == '__main__':
    test_no_superior_ball()
