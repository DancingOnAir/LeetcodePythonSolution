class Solution:
    def minFlips(self, s: str) -> int:
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
