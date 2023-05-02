from typing import List


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        cnt = [0] * n
        for s, e in trips:
            def dfs1(u, fa):
                if u == e:
                    cnt[u] += 1
                    return True

                for v in g[u]:
                    if v != fa and dfs1(v, u):
                        cnt[u] += 1
                        return True
                return False

            dfs1(s, -1)

        def dfs2(u, fa):
            not_halve = price[u] * cnt[u]
            halve = not_halve // 2
            for v in g[u]:
                if v != fa:
                    nh, h = dfs2(v, u)
                    not_halve += min(nh, h)
                    halve += nh

            return not_halve, halve
        return min(dfs2(0, -1))


def test_minimum_total_price():
    solution = Solution()
    assert solution.minimumTotalPrice(4, [[0, 1], [1, 2], [1, 3]], [2, 2, 10, 6],
                                      [[0, 3], [2, 1], [2, 3]]) == 23, 'wrong result'
    assert solution.minimumTotalPrice(2, [[0, 1]], [2, 2], [[0, 0]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_total_price()
