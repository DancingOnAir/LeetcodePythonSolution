from functools import lru_cache


class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        N = list(map(int, str(N)))

        @lru_cache(None)
        def dp(idx, prefix, bigger, repeat, digits):
            if idx == len(N):
                return 0
            if repeat and not bigger and not prefix:
                return 10 + 10 * dp(idx + 1, False, False, True, digits)
            res = 0
            for i in range(1 if not idx else 0, 10):
                _prefix = prefix and i == N[idx]
                _bigger = bigger or (prefix and i > N[idx])
                _digits = digits | (1 << i)
                _repeat = repeat

                if (digits >> i) & 1:
                    _repeat = True
                if _repeat and not (_bigger and idx == len(N) - 1):
                    res += 1
                res += dp(idx + 1, _prefix, _bigger, _repeat, _digits)

            return res

        return dp(0, True, False, False, 0)


def test_num_duplicate_digits_at_most_n():
    solution = Solution()
    assert solution.numDupDigitsAtMostN(20) == 1, 'wrong result'
    assert solution.numDupDigitsAtMostN(100) == 10, 'wrong result'
    assert solution.numDupDigitsAtMostN(1000) == 262, 'wrong result'


if __name__ == '__main__':
    test_num_duplicate_digits_at_most_n()
