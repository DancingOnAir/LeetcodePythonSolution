from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stk = list()
        for i, v in enumerate(nums * 2):
            while stk and nums[stk[-1] % n] < v:
                j = stk.pop()
                if j >= n:
                    continue
                res[j] = v
            stk.append(i)
        return res


def test_next_greater_elements():
    solution = Solution()
    assert solution.nextGreaterElements([5, 4, 3, 2, 1]) == [-1, 5, 5, 5, 5], 'wrong result'
    assert solution.nextGreaterElements([1, 2, 1]) == [2, -1, 2], 'wrong result'
    assert solution.nextGreaterElements([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4], 'wrong result'


if __name__ == '__main__':
    test_next_greater_elements()
