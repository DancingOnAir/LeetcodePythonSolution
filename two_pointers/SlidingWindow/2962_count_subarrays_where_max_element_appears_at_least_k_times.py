from typing import List
from collections import Counter


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        res, left, cnt = 0, 0, 0
        for right, x in enumerate(nums):
            cnt += (mx == x)
            while cnt >= k:
                cnt -= (nums[left] == mx)
                left += 1
            res += left
        return res

    def countSubarrays1(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        mx_val, mx_cnt = sorted(freq.items(), reverse=True)[0]
        if mx_cnt < k:
            return 0

        n, left, cnt, res = len(nums), 0, 0, 0

        for right, x in enumerate(nums):
            if x == mx_val:
                cnt += 1

            while left <= right and cnt == k:
                res += n - right
                if nums[left] == mx_val:
                    cnt -= 1
                left += 1

        return res


def test_count_subarrays():
    solution = Solution()
    assert solution.countSubarrays([1, 3, 2, 3, 3], 2) == 6, 'wrong result'
    assert solution.countSubarrays([1, 4, 2, 1], 3) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_subarrays()
