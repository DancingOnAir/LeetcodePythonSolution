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

    def sort_top_down(self, nums, lo, hi):
        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2
        self.sort_top_down(nums, lo, mid)
        self.sort_top_down(nums, mid + 1, hi)

        if nums[mid] > nums[mid + 1]:
            self.merge(nums, lo, mid, hi)

    def sort_bottom_up(self, nums):
        sz = 1
        while sz <= len(nums):
            i = 0
            while i < len(nums):
                self.merge(nums, i, i + sz - 1, min(i + sz + sz - 1, len(nums) - 1))
                i += sz + sz
            sz += sz

    def sortArray(self, nums: List[int]) -> List[int]:
        # self.sort_top_down(nums, 0, len(nums) - 1)
        self.sort_bottom_up(nums)
        return nums


def test_sort_array():
    solution = Solution()
    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5], 'wrong result'
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5], 'wrong result'


if __name__ == '__main__':
    test_sort_array()
