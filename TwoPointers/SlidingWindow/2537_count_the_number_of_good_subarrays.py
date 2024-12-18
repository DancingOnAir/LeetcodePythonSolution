from typing import List
from collections import Counter


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        res = left = pairs = 0
        for right, x in enumerate(nums):
            pairs += cnt[x]
            cnt[x] += 1
            while pairs >= k:
                cnt[nums[left]] -= 1
                pairs -= cnt[nums[left]]
                left += 1
            res += left
        return res


def test_count_good():
    solution = Solution()
    assert solution.countGood([1, 1, 1, 1, 1], 10) == 1, 'wrong result'
    assert solution.countGood([3, 1, 4, 3, 2, 2, 4], 2) == 4, 'wrong result'


if __name__ == '__main__':
    test_count_good()
