from typing import List
from heapq import heappop, heappush


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        stk1 = list()
        stk2 = list()
        res = [-1] * len(nums)

        for i, x in enumerate(nums):
            while stk2 and nums[stk2[-1]] < x:
                res[stk2.pop()] = x

            tmp = list()
            while stk1 and nums[stk1[-1]] < x:
                tmp.append(stk1.pop())

            stk1.append(i)
            stk2 += tmp[::-1]

        return res


def test_second_greater_element():
    solution = Solution()
    assert solution.secondGreaterElement([2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1], 'wrong result'
    assert solution.secondGreaterElement([3, 3]) == [-1, -1], 'wrong result'


if __name__ == '__main__':
    test_second_greater_element()
