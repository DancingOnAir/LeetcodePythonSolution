class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        m = set()
        i = 0
        x = 1
        while x < 2 ** 15:
            m.add(bin(x)[2:])
            i += 1
            x = pow(5, i)

        n = len(s)
        res = n + 1
        path = []

        def dfs(i):
            if i == n:
                nonlocal res
                res = min(res, len(path))
                return

            for j in range(n, i, -1):
                if s[i: j] in m:
                    path.append(s[i: j])
                    dfs(j)
                    path.pop()
        dfs(0)
        return res if res < n + 1 else -1


def test_minimum_beautiful_substrings():
    solution = Solution()
    # assert solution.minimumBeautifulSubstrings("1011") == 2, 'wrong result'
    # assert solution.minimumBeautifulSubstrings("111") == 3, 'wrong result'
    assert solution.minimumBeautifulSubstrings("0") == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_beautiful_substrings()
