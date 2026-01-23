from typing import List


class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            m = set()
            tot = 0
            for x in nums[i:]:
                tot += x
                m.add(x)
                if tot in m:
                    res += 1
        return res


def test_centered_subarrays():
    solution = Solution()
    assert solution.centeredSubarrays([-1, 1, 0]) == 5, 'wrong result'
    assert solution.centeredSubarrays([2, -3]) == 2, 'wrong result'


if __name__ == '__main__':
    test_centered_subarrays()
