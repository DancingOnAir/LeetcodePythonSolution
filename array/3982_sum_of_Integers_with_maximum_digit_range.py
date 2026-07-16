class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_range = res = 0
        for x in nums:
            digits = str(x)
            r = int(max(digits)) - int(min(digits))
            if r > max_range:
                max_range = r
                res = x
            elif r == max_range:
                res += x
        return res

    def maxDigitRange1(self, nums: list[int]) -> int:
        def helper(num: int) -> int:
            mx, mn = 0, 9
            while num > 0:
                r = num % 10
                num //= 10
                mx = max(mx, r)
                mn = min(mn, r)
            return mx - mn

        res = [0] * 10
        for x in nums:
            res[helper(x)] += x

        for x in res[::-1]:
            if x > 0:
                return x
        return 0


def test_max_digit_range():
    solution = Solution()
    assert solution.maxDigitRange([5724,111,350]) == 6074, 'wrong result'
    assert solution.maxDigitRange([90,900]) == 990, 'wrong result'


if __name__ == '__main__':
    test_max_digit_range()
