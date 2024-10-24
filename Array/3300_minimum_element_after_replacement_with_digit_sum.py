from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, str(x))) for x in nums)

    def minElement1(self, nums: List[int]) -> int:
        res = float('inf')
        for x in nums:
            cur = 0
            for c in str(x):
                cur += int(c)
            res = min(res, cur)
        return res


def test_min_element():
    solution = Solution()
    assert solution.minElement([10, 12, 13, 14]) == 1, 'wrong result'
    assert solution.minElement([1, 2, 3, 4]) == 1, 'wrong result'
    assert solution.minElement([999, 19, 199]) == 10, 'wrong result'


if __name__ == '__main__':
    test_min_element()
