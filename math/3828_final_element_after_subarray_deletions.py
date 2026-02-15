from typing import List


class Solution:
    def finalElement(self, nums: List[int]) -> int:
        return max(nums[0], nums[-1])


def test_final_element():
    solution = Solution()
    assert solution.finalElement([1, 5, 2]) == 2, 'wrong result'
    assert solution.finalElement([3, 7]) == 7, 'wrong result'


if __name__ == '__main__':
    test_final_element()
