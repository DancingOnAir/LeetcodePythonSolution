from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2


def test_result_array():
    solution = Solution()
    assert solution.resultArray([2, 1, 3]) == [2, 3, 1], 'wrong result'
    assert solution.resultArray([5, 4, 3, 8]) == [5, 3, 4, 8], 'wrong result'


if __name__ == '__main__':
    test_result_array()
