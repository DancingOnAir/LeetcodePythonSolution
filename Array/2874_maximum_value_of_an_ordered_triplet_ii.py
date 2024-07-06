from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = maxa = maxab = 0
        for a in nums:
            res = max(res, maxab * a)
            maxab = max(maxab, maxa - a)
            maxa = max(maxa, a)
        return res


def test_maximum_triplet_value():
    solution = Solution()
    assert solution.maximumTripletValue([12, 6, 1, 2, 7]) == 77, 'wrong result'
    assert solution.maximumTripletValue([1, 10, 3, 4, 19]) == 133, 'wrong result'
    assert solution.maximumTripletValue([1, 2, 3]) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_triplet_value()
