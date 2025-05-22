from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = odd_cnt = left = right = 0

        while right < len(nums):
            if nums[right] & 1:
                odd_cnt += 1
            right += 1

            if odd_cnt == k:
                tmp = right
                while right < len(nums) and nums[right] % 2 == 0:
                    right += 1
                right_even_cnt = right - tmp

                left_even_cnt = 0
                while nums[left] % 2 == 0:
                    left_even_cnt += 1
                    left += 1
                res += (left_even_cnt + 1) * (right_even_cnt + 1)
                left += 1
                odd_cnt -= 1
        return res


def test_number_of_subarrays():
    solution = Solution()
    assert solution.numberOfSubarrays([1, 1, 2, 1, 1], k=3) == 2, 'wrong result'
    assert solution.numberOfSubarrays([2, 4, 6], k=1) == 0, 'wrong result'
    assert solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2) == 16, 'wrong result'


if __name__ == '__main__':
    test_number_of_subarrays()
