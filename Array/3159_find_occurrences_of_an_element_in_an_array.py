from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        pos = []
        for i, v in enumerate(nums):
            if v == x:
                pos.append(i)

        res = [-1] * len(queries)
        for i, v in enumerate(queries):
            if v <= len(pos):
                res[i] = pos[v - 1]
        return res


def test_occurrences_of_element():
    solution = Solution()
    assert solution.occurrencesOfElement([1, 3, 1, 7], [1, 3, 2, 4], 1) == [0, -1, 2, -1], 'wrong result'
    assert solution.occurrencesOfElement([1, 2, 3], [10], 5) == [-1], 'wrong result'


if __name__ == '__main__':
    test_occurrences_of_element()
