class Solution:
    # |..left..|..middle..|..right..|
    # For left and right we paid just their lengths.
    # For middle we pay twice number of ones se have inside,
    # so we have: len(left) + 2* count(middle, 1) + len(right)
    # = len(left) + len(middle) + len(right) + 2*count(middle, 1) - len(middle)
    # = n + count(middle, 1) - count(middle, 0).
    def minimumTime(self, s: str) -> int:
        def min_sum(nums):
            dp = dp_min = float('inf')
            for num in nums:
                dp = min(num, dp + num)
                dp_min = min(dp, dp_min)
            return min(0, dp_min)
        return len(s) + min_sum([1 if x == '1' else -1 for x in s])


def test_minimum_time():
    solution = Solution()
    assert solution.minimumTime('1100101') == 5, 'wrong result'
    assert solution.minimumTime('0010') == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_time()
