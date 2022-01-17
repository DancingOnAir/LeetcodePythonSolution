from typing import List


class Solution:
    # def merge(self, nums, lo, mid, hi):
    #     i, j = lo, mid + 1
    #     aux = list()
    #
    #     while i <= mid and j <= hi:
    #         if nums[i][0] < nums[j][0]:
    #             aux.append(nums[i])
    #             i += 1
    #         else:
    #             less_than = i - lo
    #             while i <= mid and nums[i][0] == nums[j][0]:
    #                 aux.append(nums[i])
    #                 i += 1
    #
    #             greater_than = mid - i + 1
    #             val = nums[j][0]
    #             while j <= hi and nums[j][0] == val:
    #                 nums[j][1] += less_than
    #                 nums[j][2] += greater_than
    #                 aux.append(nums[j])
    #                 j += 1
    #
    #     while i <= mid:
    #         aux.append(nums[i])
    #         i += 1
    #     while j <= hi:
    #         nums[j][1] += mid - lo + 1
    #         aux.append(nums[j])
    #         j += 1
    #
    #     m = 0
    #     for k in range(lo, hi+1):
    #         nums[k] = aux[m]
    #         m += 1
    #     # aux = nums[lo: hi+1]
    #
    #     # for k in range(lo, hi+1):
    #     #     if i > mid:
    #     #         aux[j - lo][1] += mid - lo + 1
    #     #         nums[k] = aux[j - lo]
    #     #         j += 1
    #     #     elif j > hi:
    #     #         nums[k] = aux[i - lo]
    #     #         i += 1
    #     #     elif aux[i - lo][0] <= aux[j - lo][0]:
    #     #         nums[k] = aux[i - lo]
    #     #         i += 1
    #     #     else:
    #     #         less_than = i - lo
    #     #         greater_than = mid - i + 1
    #     #
    #     #         aux[j - lo][1] += less_than
    #     #         aux[j - lo][2] += greater_than
    #     #         nums[k] = aux[j - lo]
    #     #         j += 1
    #
    # def sort(self, nums, lo, hi):
    #     if lo >= hi:
    #         return
    #
    #     mid = lo + (hi - lo) // 2
    #     self.sort(nums, lo, mid)
    #     self.sort(nums, mid + 1, hi)
    #     # if nums[mid] > nums[mid + 1]:
    #     self.merge(nums, lo, mid, hi)

    def createSortedArray(self, instructions: List[int]) -> int:
        repeat = dict()
        id = list(range(len(instructions)))
        self.sort(data, 0, len(instructions) - 1)

        mod = 10 ** 9 + 7
        res = 0
        for i in range(len(instructions)):

            res %= mod

        return res


def test_create_sorted_array():
    solution = Solution()

    assert solution.createSortedArray([1, 5, 6, 2]) == 1, 'wrong result'
    assert solution.createSortedArray([1, 2, 3, 6, 5, 4]) == 3, 'wrong result'
    assert solution.createSortedArray([1, 3, 3, 3, 2, 4, 2, 1, 2]) == 4, 'wrong result'


if __name__ == '__main__':
    test_create_sorted_array()
