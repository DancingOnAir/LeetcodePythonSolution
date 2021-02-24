from functools import lru_cache


class Solution:
    # Why can I use fibonacci numbers?
    # a(n) = the number of valid integers less than 2^n
    # a(5) = the number of valid integers less than 0b100000, aka 0bXXXXX.
    # It equals to the number of valid integers in [0b0, 0b10000[ and in [0b10000, 0b11000[.
    # The number of valid integers [0b0, 0b10000[, which is like '0b0XXXX', equals to a(4).
    # The number of valid integers [0b10000, 0b11000[, which is like '0b101XX', equals to a(3).
    # So a(5) = a(4) + a(3).
    # Since we have checked the consecutive 1s in the loop, and the biggest number of the range must be just
    # smaller than n by 1, count+1 includes the n must be itself and has no consecutive.
    # If n has consecutive 1, count must be returned by if (pre_bit) return ans; in the loop.
    def findIntegers(self, num: int) -> int:
        f = [1, 2] + [0] * 30
        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]

        res = 0
        last_bit = 0
        k = 30
        while k >= 0:
            if num & (1 << k):
                res += f[k]
                if last_bit:
                    return res
                last_bit = 1
            else:
                last_bit = 0

            k -= 1
        return res + 1

    # digit dp
    def findIntegers1(self, num: int) -> int:
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
