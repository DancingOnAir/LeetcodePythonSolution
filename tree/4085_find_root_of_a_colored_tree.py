class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        m = {'W': 0, 'R': 1, 'B': 2}
        n = len(colors)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        res = -1
        for u, to in enumerate(g):
            if len(to) > 3:
                return -1

            cnt = [0] * 3
            for  v in to:
                cnt[m[colors[v]]] += 1

            color_u = m[colors[u]]
            if cnt[color_u] > 0 or cnt[color_u - 1] > 1:
                return -1
            if len(to) < 3 and cnt[color_u - 1] == 0:
                res = u
        return res


def test_find_colored_root():
    solution = Solution()
    assert solution.findColoredRoot([[3, 1], [3, 2], [1, 4], [2, 0]], colors="BRRWB") == 3, 'wrong result'
    assert solution.findColoredRoot([[0, 1], [1, 2], [2, 3]], colors="RBRB") == -1, 'wrong result'


if __name__ == '__main__':
    test_find_colored_root()
