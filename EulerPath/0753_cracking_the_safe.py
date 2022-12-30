from collections import defaultdict


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        highest = 10 ** (n - 1)
        seen = set()
        res = list()

        def dfs(u):
            for i in range(k):
                v = u * 10 + i
                if v not in seen:
                    seen.add(v)
                    dfs(v % highest)
                    res.append(str(i))

        dfs(0)
        return ''.join(res) + '0' * (n - 1)


def test_crack_safe():
    solution = Solution()
    assert solution.crackSafe(2, 3) == "10", 'wrong result'
    assert solution.crackSafe(1, 2) == "10", 'wrong result'
    assert solution.crackSafe(2, 2) == "01100", 'wrong result'


if __name__ == '__main__':
    test_crack_safe()
