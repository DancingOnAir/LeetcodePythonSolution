from typing import List


class Solution:
    def merge(self, nums, lo, mid, hi):
        i, j = lo, mid + 1
        aux = nums[lo: hi+1]

        for k in range(lo, hi+1):
            if i > mid:
                nums[k] = aux[j - lo]
                j += 1
            elif j > hi:
                nums[k] = aux[i - lo]
                i += 1
            elif aux[i - lo] > aux[j - lo]:
                nums[k] = aux[j - lo]
                j += 1
            else:
                nums[k] = aux[i - lo]
                i += 1

    def sort(self, nums, lo, hi):
        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2
        self.sort(nums, lo, mid)
        self.sort(nums, mid + 1, hi)

        if nums[mid] > nums[mid + 1]:
            self.merge(nums, lo, mid, hi)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums, 0, len(nums) - 1)
        return nums


def test_sort_array():
    solution = Solution()
    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5], 'wrong result'
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5], 'wrong result'


if __name__ == '__main__':
    test_sort_array()
