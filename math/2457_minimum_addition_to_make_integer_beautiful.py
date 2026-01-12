class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        origin = n
        i = 0
        while sum(map(int, str(n))) > target:
            n = n // 10 + 1
            i += 1
        return n * (10 ** i) - origin

    def makeIntegerBeautiful1(self, n: int, target: int) -> int:
        digits = []
        base = 10
        while n:
            digits.append(n % base)
            n //= base
        ds = sum(digits)
        if ds <= target:
            return 0

        i = pre_sum = pre_digit = 0
        while ds > target:
            if ds - digits[i] - pre_digit + 1 <= target:
                return 10 ** (i + 1) - digits[i] * (10 ** i) - pre_sum
            pre_digit += digits[i]
            pre_sum += digits[i] * (10 ** i)
            i += 1
        return -1


def test_make_integer_beautiful():
    solution = Solution()
    assert solution.makeIntegerBeautiful(16, 6) == 4, 'wrong result'
    assert solution.makeIntegerBeautiful(467, 6) == 33, 'wrong result'
    assert solution.makeIntegerBeautiful(1, 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_make_integer_beautiful()
