class Solution:
    # slide window
    # double string for circular array.
    # eg. s = '111000', s*2 = '111000111000', for start = 2, s' = '11|100011|1000', namely s' = '100011'
    def minFlips(self, s: str) -> int:
        n = len(s)
        s *= 2
        res_start_with_zero = res_start_with_one = 0
        res = float('inf')

        for i in range(n * 2):
            if i % 2 != int(s[i]):
                res_start_with_zero += 1
            if (i + 1) % 2 != int(s[i]):
                res_start_with_one += 1

            if i >= n:
                if (i - n) % 2 != int(s[i - n]):
                    res_start_with_zero -= 1
                if (i - n + 1) % 2 != int(s[i - n]):
                    res_start_with_one += 1
            if i >= n - 1:
                res = min(res, res_start_with_zero, res_start_with_one)
        return res

    # count number of '1' on even & odd positions
    def minFlips1(self, s: str) -> int:
        n = len(s)
        even_ones = odd_ones = 0
        for i, c in enumerate(s):
            if i % 2 == 1 and c == '1':
                odd_ones += 1
            elif i % 2 == 0 and c == '1':
                even_ones += 1

        if n % 2 == 0:
            return min(even_ones + n // 2 - odd_ones, odd_ones + n // 2 - even_ones)
        # 1st element is '0' then op2 should be even_ones + n // 2 - odd_ones
        # 1st element is '1' then op2 should be odd_ones + n // 2 + 1 - even_ones
        res = min(even_ones + n // 2 - odd_ones, odd_ones + n // 2 + 1 - even_ones)
        for i in range(n):
            if s[i] == '1':
                even_ones, odd_ones = odd_ones + 1, even_ones - 1
                res = min(res, min(even_ones + n // 2 - odd_ones, odd_ones + n // 2 + 1 - even_ones))
            else:
                even_ones, odd_ones = odd_ones, even_ones
                res = min(res, min(even_ones + n // 2 - odd_ones, odd_ones + n // 2 + 1 - even_ones))
        return res


def test_min_flips():
    solution = Solution()
    #
    assert solution.minFlips('10001100101000000') == 5, 'wrong result'
    assert solution.minFlips('111000') == 2, 'wrong result'
    assert solution.minFlips('010') == 0, 'wrong result'
    assert solution.minFlips('1110') == 1, 'wrong result'


if __name__ == '__main__':
    test_min_flips()
