from typing import List


class Solution:
    # 遍历nums，计算2个元素之和并添加到set里，如果set没有重复值，那么它的长度应该等于len(nums) - 1
    def findSubarrays(self, nums: List[int]) -> bool:
        m = set()
        for i in range(1, len(nums)):
            m.add(nums[i - 1] + nums[i])
        if len(m) == len(nums) - 1:
            return False
        return True

    # 遍历nums，计算2个元素之和并添加到set里，判断set里有没有重复的
    def findSubarrays1(self, nums: List[int]) -> bool:
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
