from collections import defaultdict


class Solution:
    # https://leetcode.com/problems/cracking-the-safe/solutions/902372/easiest-explanation-and-shortest-code-beat-100/
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join(str(i) for i in range(k))
        if k == 1:
            return '0' * n

        res = '0' * (n - 1)
        seen = set()
        for i in range(k ** n):
            suffix = res[-n + 1:]
            for j in range(k - 1, -1, -1):
                if suffix + str(j) not in seen:
                    seen.add(suffix + str(j))
                    res += str(j)
                    break
        return res

    # euler path
    def crackSafe1(self, n: int, k: int) -> str:
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
    assert solution.crackSafe(1, 2) == "10", 'wrong result'
    assert solution.crackSafe(2, 2) == "01100", 'wrong result'


if __name__ == '__main__':
    test_crack_safe()
