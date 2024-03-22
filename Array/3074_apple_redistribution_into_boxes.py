from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        res, cur, tot = 0, 0, sum(apple)
        for x in sorted(capacity, reverse=True):
            res += 1
            cur += x
            if cur >= tot:
                return res
        return -1


def test_minimum_boxes():
    solution = Solution()
    assert solution.minimumBoxes([1, 3, 2], [4, 3, 1, 5, 2]) == 2, 'wrong result'
    assert solution.minimumBoxes([5, 5, 5], [2, 4, 2, 7]) == 4, 'wrong result'


if __name__ == '__main__':
    test_minimum_boxes()
