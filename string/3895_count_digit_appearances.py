class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        s = ''.join(map(str, nums))
        return s.count(str(digit))

    def countDigitOccurrences1(self, nums: list[int], digit: int) -> int:
        res = 0
        target = str(digit)
        for x in nums:
            res += sum(1 for c in str(x) if c == target)
        return res


def test_count_digit_occurrences():
    solution = Solution()
    assert solution.countDigitOccurrences([12,54,32,22], digit = 2) == 4, 'wrong result'
    assert solution.countDigitOccurrences([1,34,7], digit = 9) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_digit_occurrences()

