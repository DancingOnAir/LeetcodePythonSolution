from typing import List
from collections import defaultdict


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        left = 0
        tot = 0
        res = float('inf')
        cnt = defaultdict(int)
        for right, x in enumerate(nums):
            if cnt[x] == 0:
                tot += x
            cnt[x] += 1

            while tot >= k:
                res = min(res, right - left + 1)
                if res == 1:
                    break
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    tot -= nums[left]
                left += 1
        return res if res < float('inf') else -1


def test_min_length():
    solution = Solution()
    assert solution.minLength([63,47,9,23,47,29,47,23,36,47,9], k=121) == 4, 'wrong result'
    assert solution.minLength([2, 2, 3, 1], k=4) == 2, 'wrong result'
    assert solution.minLength([3, 2, 3, 4], k=5) == 2, 'wrong result'
    assert solution.minLength([5, 5, 4], k=5) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_length()
