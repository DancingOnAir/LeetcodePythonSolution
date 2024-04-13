from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase, decrease = 0, 0
        res, pre = 0, 0
        for x in nums:
            if pre and x <= pre:
                increase = 0
            increase += 1

            if pre and x >= pre:
                decrease = 0
            decrease += 1

            res = max(res, increase, decrease)
            pre = x
        return res

    # monoton stack
    def longestMonotonicSubarray1(self, nums: List[int]) -> int:
        increase = []
        decrease = []
        res = 0
        for x in nums:
            if increase and x <= increase[-1]:
                increase.clear()
            increase.append(x)

            if decrease and x >= decrease[-1]:
                decrease.clear()
            decrease.append(x)
            res = max(res, len(increase), len(decrease))
        return res


def test_longest_monotonic_subarray():
    solution = Solution()
    assert solution.longestMonotonicSubarray([1, 4, 3, 3, 2]) == 2, 'wrong result'
    assert solution.longestMonotonicSubarray([3, 3, 3, 3]) == 1, 'wrong result'
    assert solution.longestMonotonicSubarray([3, 2, 1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_longest_monotonic_subarray()
