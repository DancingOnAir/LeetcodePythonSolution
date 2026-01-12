from typing import List
from collections import defaultdict


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = defaultdict(int), defaultdict(int)
        left_cnt, right_cnt = defaultdict(int), defaultdict(int)
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[i] = left_cnt[nums[i]] * i - left_sum[nums[i]]
            left_sum[nums[i]] += i
            left_cnt[nums[i]] += 1

        for i in range(n - 1, -1, -1):
            res[i] += right_sum[nums[i]] - right_cnt[nums[i]] * i
            right_sum[nums[i]] += i
            right_cnt[nums[i]] += 1
        return res

    # simulation but TLE
    def distance1(self, nums: List[int]) -> List[int]:
        m = defaultdict(list)
        for i, v in enumerate(nums):
            m[v].append(i)
        return [sum(abs(x - i) for x in m[v]) for i, v in enumerate(nums)]


def test_distance():
    solution = Solution()
    assert solution.distance([1,3,1,1,2]) == [5,0,3,4,0], 'wrong result'
    assert solution.distance([0,5,3]) == [0,0,0], 'wrong result'


if __name__ == '__main__':
    test_distance()
