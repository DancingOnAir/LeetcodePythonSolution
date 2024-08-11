from typing import List
from collections import Counter, deque


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left, res = 0, 0
        min_dp, max_dp = deque(), deque()
        for right, x in enumerate(nums):
            while min_dp and min_dp[-1] > x:
                min_dp.pop()
            min_dp.append(x)
            while max_dp and max_dp[-1] < x:
                max_dp.pop()
            max_dp.append(x)

            while max_dp[0] > min_dp[0] + 2:
                if nums[left] == max_dp[0]:
                    max_dp.popleft()
                if nums[left] == min_dp[0]:
                    min_dp.popleft()
                left += 1
            res += right - left + 1

        return res

    def continuousSubarrays1(self, nums: List[int]) -> int:
        left, res = 0, 0
        freq = Counter()
        for right, x in enumerate(nums):
            freq[x] += 1
            while max(freq) > min(freq) + 2:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            res += right - left + 1
        return res


def test_continuous_subarrays():
    solution = Solution()
    assert solution.continuousSubarrays([5, 4, 2, 4]) == 8, 'wrong result'
    assert solution.continuousSubarrays([1, 2, 3]) == 6, 'wrong result'


if __name__ == '__main__':
    test_continuous_subarrays()
