class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        if 1 == n:
            return 10
        # 从最高位到最低位的可选数字个数，最高位不能为0，只能1-9，次高位可以选0-9
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        res, product = 1, 1
        for i in range(min(n, 10)):
            product *= choices[i]
            res += product
        return res

    # digit dp
    def countNumbersWithUniqueDigits1(self, n: int) -> int:
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
                # 这里控制是否符合条件：1.没有重复的数位。2.不符合大于并且已经是最低位。
                if not _repeated and not (idx == len(N) - 1 and _bigger):
                    res += 1

                _digits = digits | (1 << i)
                res += dp(idx + 1, _prefix, _bigger, _repeated, _digits)
            return res

        return dp(0, True, False, False, 0) + (1 if n > 1 else 0)


def test_count_numbers_with_unique_digits():
    solution = Solution()
    assert solution.countNumbersWithUniqueDigits(1) == 10, 'wrong result'
    assert solution.countNumbersWithUniqueDigits(2) == 91, 'wrong result'


if __name__ == '__main__':
    test_count_numbers_with_unique_digits()
