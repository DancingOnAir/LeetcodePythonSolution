from typing import List


class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        # lcp[i][n] = lcp[n][j] = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                if nums[i] == nums[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        res = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if (i <= j - i and lcp[0][i] >= i) or lcp[i][j] >= j - i:
                    res += 1
        return res


def test_beautiful_splits():
    solution = Solution()
    assert solution.beautifulSplits([1, 1, 2, 1]) == 2, 'wrong result'
    assert solution.beautifulSplits([1, 2, 3, 4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_beautiful_splits()
