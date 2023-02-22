from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = i = total = 0
        for j, v in enumerate(nums):
            total += v
            while total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1
            res += j - i + 1

        return res


def test_count_subarrays():
    solution = Solution()
    assert solution.countSubarrays([2, 1, 4, 3, 5], 10) == 6, 'wrong result'
    assert solution.countSubarrays([1, 1, 1], 5) == 5, 'wrong result'


if __name__ == '__main__':
    test_count_subarrays()
