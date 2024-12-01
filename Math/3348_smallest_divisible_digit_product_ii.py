from functools import cache
from math import gcd


class Solution:
    def smallestNumber(self, s: str, t: int) -> str:
        tmp = t
        cnt = 0
        for p in [2, 3, 5, 7]:
            while tmp % p == 0:
                tmp //= p
                cnt += 1
        if tmp != 1:
            return "-1"

        cnt = max(cnt - len(s) + 1, 1)
        s = '0' * cnt + s

        n = len(s)
        res = ['0'] * n

        @cache
        def dfs(i, t, is_limit):
            if i == n:
                return t == 1
            # 可以填入0
            if is_limit and i < cnt and dfs(i + 1, t, True):
                return True

            low = int(s[i]) if is_limit else 0
            for d in range(max(1, low), 10):
                if dfs(i + 1, t // gcd(t, d), is_limit and d == low):
                    res[i] = str(d)
                    return True
            return False

        dfs(0, t, True)
        dfs.cache_clear()
        return ''.join(res).lstrip('0')


def test_smallest_number():
    solution = Solution()
    assert solution.smallestNumber("1234", 256) == "1488", 'wrong result'
    assert solution.smallestNumber("12355", 50) == "12355", 'wrong result'
    assert solution.smallestNumber("11111", 26) == "-1", 'wrong result'


if __name__ == '__main__':
    test_smallest_number()
