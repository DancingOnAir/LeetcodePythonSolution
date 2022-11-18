class Solution:
    # |..left..|..middle..|..right..|
    # For left and right we paid just their lengths.
    # For middle we pay twice number of ones se have inside,
    # so we have: len(left) + 2* count(middle, 1) + len(right)
    # = len(left) + len(middle) + len(right) + 2*count(middle, 1) - len(middle)
    # = n + count(middle, 1) - count(middle, 0).
    def minimumTime1(self, s: str) -> int:
        def min_sum(nums):
            dp = dp_min = float('inf')
            for num in nums:
                dp = min(num, dp + num)
                dp_min = min(dp, dp_min)
            return min(0, dp_min)
        return len(s) + min_sum([1 if x == '1' else -1 for x in s])

    # left counts the cost to clear all illegal goods from s[0] to s[i]. by removing all left cars, left = i + 1
    # right counts the cost to clear all illegal goods from s[i+1] to s[n-1], right = n - i - 1
    def minimumTime(self, s: str) -> int:
        left = 0
        res = len(s)

        for i, ch in enumerate(s):
            left = min(left + (ch == '1') * 2, i + 1)
            res = min(res, left + len(s) - i - 1)
        return res


def test_minimum_time():
    solution = Solution()
    assert solution.minimumTime('1100101') == 5, 'wrong result'
    assert solution.minimumTime('0010') == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_time()
