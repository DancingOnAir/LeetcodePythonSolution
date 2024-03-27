from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        res, pre = 1, nums[0] + nums[1]
        for i in range(2, len(nums) - 1, 2):
            if (nums[i] + nums[i + 1]) == pre:
                res += 1
            else:
                break

        return res

def test_max_operations():
    solution = Solution()
    assert solution.maxOperations([3, 2, 1, 4, 5]) == 2, ' wrong result'
    assert solution.maxOperations([3, 2, 6, 1, 4]) == 1, ' wrong result'


if __name__ == '__main__':
    test_max_operations()
