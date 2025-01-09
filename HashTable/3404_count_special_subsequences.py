from typing import List
from collections import defaultdict
from math import gcd


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        suf = defaultdict(int)
        n = len(nums)
        for i in range(4, n - 2):
            c = nums[i]
            for d in nums[i + 2:]:
                g = gcd(c, d)
                suf[d//g, c//g] += 1

        res = 0
        for i in range(2, n - 4):
            b = nums[i]
            for a in nums[: i - 1]:
                g = gcd(a, b)
                res += suf[a//g, b//g]
            # 这里移除c=num[i+2]的计数，因为i+1后, c=nums[i+1]还是会计算进去
            c = nums[i + 2]
            for d in nums[i + 4:]:
                g = gcd(c, d)
                suf[d//g, c//g] -= 1
        return res


def test_number_of_subsequences():
    solution = Solution()
    assert solution.numberOfSubsequences([1, 2, 3, 4, 3, 6, 1]) == 1, 'wrong result'
    assert solution.numberOfSubsequences([3, 4, 3, 4, 3, 4, 3, 4]) == 3, 'wrong result'


if __name__ == '__main__':
    test_number_of_subsequences()
