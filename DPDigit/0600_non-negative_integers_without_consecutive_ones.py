from functools import lru_cache


class Solution:
    # digit dp
    def findIntegers(self, num: int) -> int:
        N = list(map(int, bin(num)[2:]))

        @lru_cache(None)
        def dp(idx, prefix, bigger, last_one):
            if idx == len(N):
                return 1 if not bigger else 0

            res = 0
            for bit in [0] + ([] if last_one else [1]):
                _prefix = prefix and bit == N[idx]
                _bigger = bigger or (prefix and bit and not N[idx])
                res += dp(idx + 1, _prefix, _bigger, bit == 1)

            return res

        return dp(0, True, False, 0)


def test_find_integers():
    solution = Solution()
    assert solution.findIntegers(5) == 5, 'wrong result'


if __name__ == '__main__':
    test_find_integers()
