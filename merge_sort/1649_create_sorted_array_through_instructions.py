from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList


class Solution:
    def merge(self, nums, lo, mid, hi, id, left_less):
        i, j, k = lo, mid + 1, 0
        aux = [0] * (hi - lo + 1)

        while i <= mid and j <= hi:
            if nums[id[i]] < nums[id[j]]:
                left_less[id[j]] += mid - i + 1
                aux[k] = id[j]
                k += 1
                j += 1
            else:
                aux[k] = id[i]
                k += 1
                i += 1

        while j <= hi:
            aux[k] = id[j]
            k += 1
            j += 1

        while i <= mid:
            aux[k] = id[i]
            k += 1
            i += 1

        for i in range(lo, hi+1):
            id[i] = aux[i - lo]

    def sort(self, nums, lo, hi, id, left_less):
        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2
        self.sort(nums, lo, mid, id, left_less)
        self.sort(nums, mid + 1, hi, id, left_less)
        self.merge(nums, lo, mid, hi, id, left_less)

    # merge sort solution, but TLE
    def createSortedArray1(self, instructions: List[int]) -> int:
        n = len(instructions)
        repeat = defaultdict(int)
        id = list(range(n))
        left_less = [0] * n
        self.sort(instructions, 0, len(instructions) - 1, id, left_less)

        mod = 10 ** 9 + 7
        res = 0
        for i in range(n):
            res += min(left_less[i], i - left_less[i] - repeat[instructions[i]])
            repeat[instructions[i]] += 1
            res %= mod

        return res

    # SortedList, if list.insert(i, val), it will be TLE.
    def createSortedArray(self, instructions: List[int]) -> int:
        res = 0
        nums = SortedList()

        for ins in instructions:
            res += min(nums.bisect_left(ins), len(nums) - nums.bisect_right(ins))
            res %= (10 ** 9 + 7)
            nums.add(ins)

        return res


def test_create_sorted_array():
    solution = Solution()

    assert solution.createSortedArray([1, 5, 6, 2]) == 1, 'wrong result'
    assert solution.createSortedArray([1, 2, 3, 6, 5, 4]) == 3, 'wrong result'
    assert solution.createSortedArray([1, 3, 3, 3, 2, 4, 2, 1, 2]) == 4, 'wrong result'


if __name__ == '__main__':
    test_create_sorted_array()
