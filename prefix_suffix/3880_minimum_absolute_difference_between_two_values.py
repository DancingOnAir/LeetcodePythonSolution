class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        last_one = last_two = -1
        res = float('inf')
        for i, x in enumerate(nums):
            if x == 1:
                if last_two >= 0:
                    res = min(res, i - last_two)
                last_one = i
            elif x == 2:
                if last_one >= 0:
                    res = min(res, i - last_one)
                last_two = i
        return -1 if res == float('inf') else res


def test_min_absolute_difference():
    solution = Solution()
    assert solution.minAbsoluteDifference([1, 0, 0, 2, 0, 1]) == 2, 'wrong result'
    assert solution.minAbsoluteDifference([1, 0, 1, 0]) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_absolute_difference()
