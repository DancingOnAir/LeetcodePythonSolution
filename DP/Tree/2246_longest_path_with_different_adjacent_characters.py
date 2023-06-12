from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        def dfs(p):
            nonlocal res
            x = 0

            for child in g[p]:
                y = dfs(child) + 1
                if s[child] != s[p]:
                    res = max(res, x + y)
                    x = max(x, y)
            return x

        res = 0
        dfs(0)
        # 返回的是节点数，不是边，所以加1
        return res + 1


def test_longest_path():
    solution = Solution()
    assert solution.longestPath([-1, 0, 0, 1, 1, 2], "abacbe") == 3, 'wrong result'
    assert solution.longestPath([-1, 0, 0, 0], "aabc") == 3, 'wrong result'


if __name__ == '__main__':
    test_longest_path()
