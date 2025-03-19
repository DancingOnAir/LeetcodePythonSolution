from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = 0
        for i, x in enumerate(sorted(set(nums), reverse=True)):
            if i > 0 and x < 0:
                break
            res += x
        return res


def test_max_sum():
    solution = Solution()
    assert solution.maxSum([-15,0]) == 0, 'wrong result'
    assert solution.maxSum([1,2,3,4,5]) == 15, 'wrong result'
    assert solution.maxSum([1,1,0,1,1]) == 1, 'wrong result'
    assert solution.maxSum([1,2,-1,-2,1,0,-1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_max_sum()
