from typing import List
from collections import defaultdict, Counter
from itertools import groupby


class Solution:
    # dp
    def maximumLength(self, nums: List[int]) -> int:
        dp = defaultdict(Counter)
        k = 2
        for x in nums:
            for y in range(k):
                dp[y][x % k] = max(dp[y][x % k], dp[x % k][y] + 1)
        return max(max(dp[x].values()) for x in range(k))

    def maximumLength2(self, nums: List[int]) -> int:
        nums = [x % 2 for x in nums]
        return max(nums.count(0), nums.count(1), len(list(groupby(nums))))

    def maximumLength1(self, nums: List[int]) -> int:
        # aa表示偶数子序列，bb表示奇数子序列，ab表示奇偶隔子序列
        aa = bb = ab = 0
        pre = -1
        for x in nums:
            if x & 1:
                bb += 1
                if pre == 0 or pre == -1:
                    ab += 1
            else:
                aa += 1
                if pre == 1 or pre == -1:
                    ab += 1

            pre = x & 1
        return max(aa, bb, ab)


def test_maximum_length():
    solution = Solution()
    assert solution.maximumLength([1,2,3,4]) == 4, 'wrong result'
    assert solution.maximumLength([1,2,1,1,2,1,2]) == 6, 'wrong result'
    assert solution.maximumLength([1,3]) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_length()
