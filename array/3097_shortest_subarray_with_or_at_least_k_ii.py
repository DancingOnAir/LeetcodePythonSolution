from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = [-1 for _ in range(32)]
        left, tot, n, res = 0, 0, len(nums), float('inf')
        for right in range(n):
            tot |= nums[right]

            for i in range(32):
                if (nums[right] >> i) & 1:
                    bits[i] = right
            while left <= right and tot >= k:
                res = min(res, right - left + 1)
                for i in range(32):
                    if (nums[left] >> i) & 1 and bits[i] == left:
                        bits[i] = -1
                        tot ^= (1 << i)
                left += 1

        return res if res < float('inf') else -1


def test_minimum_subarray_length():
    solution = Solution()
    assert solution.minimumSubarrayLength([1,2,3], 2) == 1, 'wrong result'
    assert solution.minimumSubarrayLength([2,1,8], 10) == 3, 'wrong result'
    assert solution.minimumSubarrayLength([1,2], 0) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_subarray_length()
