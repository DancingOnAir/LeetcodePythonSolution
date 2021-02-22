from functools import lru_cache


class Solution:
    # math
    # Basic idea: count number of combination of 1 at each digit in two cases: prefix appears or not
    # Eg.3101592:
    # 1) one at hundreds:      1 (< 5): [1~3101]1[0~99]. So # = 3101 * 100 + 100 (Safe since 31011XX never be greater than 31015XX)
    # 2) one at thousands:     1 (= 1): [1~310]1[0~592]. So # = 310 * 1000 + (592 + 1) (Unsafe if prefix is 0, it must be <= 1592)
    # 3) one at ten thousands: 1 (> 0): [1~30]1[0~9999]. So # = 30 * 10000 (If prefix is 0, no 1 digit number exist)
    def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0

        res, i = 0, 1
        while i <= n:
            pre = n // (i * 10)
            cur = (n // i) % 10
            suf = n % i

            res += pre * i
            if cur > 1:
                res += i
            elif cur == 1:
                res += suf + 1

            i *= 10
        return res

    # https://codeforces.com/blog/entry/53960
    def countDigitOne1(self, n: int) -> int:
        if n < 1:
            return 0

        N = list(map(int, str(n)))

        @lru_cache(None)
        def dp(idx, prefix, bigger, ones):
            if idx == len(N):
                return 0

            res = 0
            # the highest significant cannot be 0
            for i in range(0 if idx > 0 else 1, 10):
                _prefix = prefix and i == N[idx]
                _bigger = bigger or (prefix and i > N[idx])
                _ones = ones + (1 if i == 1 else 0)
                # add previous 1s, notice: it's ones not _ones
                if not (idx == len(N) - 1 and _bigger):
                    res += ones

                if i == 1 and not (idx == len(N) - 1 and _bigger):
                    res += 1

                res += dp(idx + 1, _prefix, _bigger, _ones)
            return res

        return dp(0, True, False, 0)


def test_count_digit_one():
    solution = Solution()
    assert solution.countDigitOne(13) == 6, 'wrong result'
    assert solution.countDigitOne(0) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_digit_one()
