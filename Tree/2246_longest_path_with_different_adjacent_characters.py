from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)

        def dfs(i: int) -> int:
            nonlocal res
            max_len = 0
            for j in tree[i]:
                cur_len = dfs(j) + 1
                if s[i] != s[j]:
                    res = max(res, max_len + cur_len)
                    max_len = max(max_len, cur_len)
            return max_len

        res = 0
        dfs(0)
        return res + 1


def test_longest_path():
    solution = Solution()
    assert solution.longestPath([-1, 0, 0, 1, 1, 2], "abacbe") == 3, 'wrong result'
    assert solution.longestPath([-1, 0, 0, 0], "aabc") == 3, 'wrong result'


if __name__ == '__main__':
    test_longest_path()
