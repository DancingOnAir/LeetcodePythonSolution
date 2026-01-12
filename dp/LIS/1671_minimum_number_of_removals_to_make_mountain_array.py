from typing import List
from bisect import bisect_left


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        def LIS(arr):
            g = list()
            for x in arr:
                i = bisect_left(g, x)
                if i == len(g):
                    g.append(x)
                else:
                    g[i] = x
            return len(g)

        res = n
        for i in range(1, n - 1):
            l, r = LIS(nums[:i + 1]), LIS(nums[i:][::-1])
            # 必须保证左右的LIS长度为2，为1的话可能是最大值，左边或右边为空
            if l < 2 or r < 2:
                continue
            res = min(res, n - l - r + 1)
        return res


def test_minimum_mountain_removals():
    solution = Solution()
    assert solution.minimumMountainRemovals([9,8,1,7,6,5,4,3,2,1]) == 2, 'wrong result'
    assert solution.minimumMountainRemovals([1, 2, 3, 4, 4, 3, 2, 1]) == 1, 'wrong result'
    assert solution.minimumMountainRemovals([1, 3, 1]) == 0, 'wrong result'
    assert solution.minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_minimum_mountain_removals()
