from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        m = set()
        for i, val in enumerate(nums):
            if i > 0:
                if nums[i - 1] + nums[i] in m:
                    return True
                m.add(nums[i - 1] + nums[i])
        return False


def test_find_subarrays():
    solution = Solution()
    assert solution.findSubarrays([4, 2, 4]), 'wrong result'
    assert not solution.findSubarrays([1, 2, 3, 4, 5]), 'wrong result'
    assert solution.findSubarrays([0, 0, 0]), 'wrong result'


if __name__ == '__main__':
    test_find_subarrays()
