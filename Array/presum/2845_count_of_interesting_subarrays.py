from typing import List
from collections import Counter


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res = acc = 0
        cnt = Counter({0: 1})
        for x in nums:
            acc = (acc + (1 if x % modulo == k else 0)) % modulo
            # if (y-x) % M == k, then (y-k) % M == x % M
            # Current we have acc elements of A[i] % mod == k,
            # We want to find the prefix subarray where have (acc - k) elements of A[i] % mod == k.
            res += cnt[(acc - k) % modulo]
            cnt[acc] += 1
        return res


def test_count_interesting_subarrays():
    solution = Solution()
    # assert solution.countInterestingSubarrays([3, 2, 4], modulo=2, k=1) == 3, 'wrong result'
    assert solution.countInterestingSubarrays([3, 1, 9, 6], modulo=3, k=0) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_interesting_subarrays()
