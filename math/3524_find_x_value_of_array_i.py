from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        dp = [[0] * k for _ in range(len(nums) + 1)]
        for i, v in enumerate(nums):
            dp[i + 1][v % k] = 1
            for y, c in enumerate(dp[i]):
                dp[i + 1][y * v % k] += c
            for x, c in enumerate(dp[i + 1]):
                res[x] += c
        return res


def test_result_array():
    solution = Solution()
    assert solution.resultArray([1, 2, 3, 4, 5], k=3) == [9, 2, 4], 'wrong result'
    assert solution.resultArray([1, 2, 4, 8, 16, 32], k=4) == [18, 1, 2, 0], 'wrong result'
    assert solution.resultArray([1, 1, 2, 1, 1], k=2) == [9, 6], 'wrong result'


if __name__ == '__main__':
    test_result_array()
