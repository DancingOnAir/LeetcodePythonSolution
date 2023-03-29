from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        res = list()
        total = sum(nums)
        left_sum = 0
        for x in nums:
            res.append(abs(total - x - left_sum - left_sum))
            left_sum += x
        return res


def test_left_right_difference():
    solution = Solution()
    assert solution.leftRigthDifference([10,4,8,3]) == [15,1,11,22]
    assert solution.leftRigthDifference([1]) == [0]


if __name__ == '__main__':
    test_left_right_difference()
