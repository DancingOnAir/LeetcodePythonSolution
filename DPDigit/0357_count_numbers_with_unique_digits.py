class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        N = [1] + [0] * n

        def dp(idx, prefix, bigger, repeated, digits):
            if idx == len(N):
                return 0
            if not repeated and not prefix and not bigger:
                return 10 + 10 * dp(idx + 1, False, False, True, digits)

            res = 0
            for i in range(1 if not idx else 0, 10):
                _prefix = prefix and i == N[idx]
                _bigger = bigger or (prefix and i > N[idx])
                _repeated = repeated
                # check current digit whether exists in digits.
                if (digits >> i) & 1:
                    _repeated = True
                if not _repeated and not (idx == len(N) - 1 and _bigger):
                    res += 1

                _digits = digits | (1 << i)
                res += dp(idx + 1, _prefix, _bigger, _repeated, _digits)
            return res

        return dp(0, True, False, False, 0) + (1 if n > 1 else 0)


def test_count_numbers_with_unique_digits():
    solution = Solution()
    assert solution.countNumbersWithUniqueDigits(2) == 91, 'wrong result'


if __name__ == '__main__':
    test_count_numbers_with_unique_digits()
