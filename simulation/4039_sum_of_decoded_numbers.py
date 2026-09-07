class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        for x in nums:
            d = x // 10
            length_d = 0
            v = d
            while v != 0:
                length_d += 1
                v //= 10
            pow10 = 10 ** (length_d - x % 10)
            res += pow(d // pow10, d % pow10, MOD)
        return res % MOD


def test_sum_decoded():
    solution = Solution()
    assert solution.sumDecoded([231]) == 8, 'wrong result'
    assert solution.sumDecoded([2522, 2101]) == 1649, 'wrong result'
    assert solution.sumDecoded([2301]) == 73741817, 'wrong result'


if __name__ == '__main__':
    test_sum_decoded()
