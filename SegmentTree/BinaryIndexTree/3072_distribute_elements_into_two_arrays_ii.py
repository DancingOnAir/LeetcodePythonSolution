from typing import List
from sortedcontainers import SortedList
from bisect import bisect_left


class Fenwick:
    def __init__(self, n):
        self.tree = [0] * n

    # 把下标为i的元素个数+1
    def add(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    # 计算下标在[1, i]的元素个数之和
    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res


class Solution:
    # Binary Index Tree
    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        n = len(sorted_nums)
        t1, t2 = Fenwick(n + 1), Fenwick(n + 1)
        t1.add(bisect_left(sorted_nums, nums[0]) + 1)
        t2.add(bisect_left(sorted_nums, nums[1]) + 1)
        arr1, arr2 = [nums[0]], [nums[1]]

        for x in nums[2:]:
            v = bisect_left(sorted_nums, x) + 1
            # 分别计算arr中大于v的元素个数
            cnt1 = len(arr1) - t1.query(v)
            cnt2 = len(arr2) - t2.query(v)

            if cnt1 > cnt2 or (cnt1 == cnt2 and len(arr1) <= len(arr2)):
                arr1.append(x)
                t1.add(v)
            else:
                arr2.append(x)
                t2.add(v)

        return arr1 + arr2

    # sorted container
    def resultArray1(self, nums: List[int]) -> List[int]:
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
