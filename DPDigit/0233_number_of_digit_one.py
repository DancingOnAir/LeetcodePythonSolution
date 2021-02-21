# https://codeforces.com/blog/entry/53960
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0

        N = list(map(int, str(n)))

        def dp(idx, prefix, bigger, ones):
            if idx == len(N):
                return 0

            res = 0
            # the highest significant cannot be 0
            for i in range(0 if idx > 0 else 1, 10):
                _prefix = prefix and i == N[idx]
                _bigger = bigger or (prefix and i > N[idx])
                _ones = ones + (1 if i == 1 else 0)

                if not (idx == len(N) - 1 and _bigger):
                    res += ones

                if i == 1 and not (idx == len(N) - 1 and _bigger):
                    res += 1

                res += dp(idx + 1, _prefix, _bigger, _ones)
            return res

        return dp(0, True, False, 0)


def test_count_digit_one():
    solution = Solution()


if __name__ == '__main__':
    test_count_digit_one()
