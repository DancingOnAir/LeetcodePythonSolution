from typing import List
from sortedcontainers import SortedList


class Solution:
    # segment tree
    # def resultArray(self, nums: List[int]) -> List[int]:

    # sorted container
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        sorted_arr1, sorted_arr2 = SortedList([nums[0]]), SortedList([nums[1]])
        for i in range(2, len(nums)):
            cnt1 = len(sorted_arr1) - sorted_arr1.bisect_right(nums[i])
            cnt2 = len(sorted_arr2) - sorted_arr2.bisect_right(nums[i])

            if cnt1 > cnt2:
                sorted_arr1.add(nums[i])
                arr1.append(nums[i])
            elif cnt1 < cnt2:
                sorted_arr2.add(nums[i])
                arr2.append(nums[i])
            elif len(arr1) <= len(arr2):
                sorted_arr1.add(nums[i])
                arr1.append(nums[i])
            else:
                sorted_arr2.add(nums[i])
                arr2.append(nums[i])

        return arr1 + arr2


def test_result_array():
    solution = Solution()
    assert solution.resultArray([2, 1, 3, 3]) == [2, 3, 1, 3], 'wrong result'
    assert solution.resultArray([5, 14, 3, 1, 2]) == [5, 3, 1, 2, 14], 'wrong result'
    assert solution.resultArray([3, 3, 3, 3]) == [3, 3, 3, 3], 'wrong result'


if __name__ == '__main__':
    test_result_array()
