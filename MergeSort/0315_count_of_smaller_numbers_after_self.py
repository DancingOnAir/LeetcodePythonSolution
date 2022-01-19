from typing import List


class Solution:
    def merge(self, nums, lo, mid, hi, right_less, index):
        i, j = lo, mid + 1
        aux = [0] * (hi - lo + 1)

        for k in range(lo, hi+1):
            if i > mid:
                aux[k - lo] = index[j]
                j += 1
            elif j > hi:
                right_less[index[i]] += hi - mid
                aux[k - lo] = index[i]
                i += 1
            elif nums[index[i]] <= nums[index[j]]:
                right_less[index[i]] += j - mid - 1
                aux[k - lo] = index[i]
                i += 1
            else:
                aux[k - lo] = index[j]
                j += 1

        for i in range(lo, hi+1):
            index[i] = aux[i - lo]

    def sort(self, nums, lo, hi, right_less, index):
        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2
        self.sort(nums, lo, mid, right_less, index)
        self.sort(nums, mid + 1, hi, right_less, index)
        if nums[index[mid]] > nums[index[mid + 1]]:
            self.merge(nums, lo, mid, hi, right_less, index)

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        index = list(range(n))

        self.sort(nums, 0, n - 1, res, index)

        return res


def test_count_smaller():
    solution = Solution()
    assert solution.countSmaller([2, 0, 1]) == [2, 0, 0], 'wrong result'
    assert solution.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0], 'wrong result'
    assert solution.countSmaller([-1]) == [0], 'wrong result'
    assert solution.countSmaller([-1, -1]) == [0, 0], 'wrong result'


if __name__ == '__main__':
    test_count_smaller()
