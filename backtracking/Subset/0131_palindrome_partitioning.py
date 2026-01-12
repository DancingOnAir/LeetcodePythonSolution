from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 0:
            return []

        res = []
        path = []

        def dfs(i):
            if i == n:
                res.append(path.copy())
                return

            for j in range(i, n):
                t = s[i: j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()
        dfs(0)
        return res


def test_partition():
    solution = Solution()
    assert solution.partition("aab") == [["a", "a", "b"], ["aa", "b"]], 'wrong result'
    assert solution.partition("a") == [["a"]], 'wrong result'


if __name__ == '__main__':
    test_partition()
