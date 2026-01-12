from typing import List


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        mx = max(groups)
        target = [-1] * (mx + 1)
        for i, x in enumerate(elements):
            if x > mx or target[x] >= 0:
                continue
            for y in range(x, mx + 1, x):
                if target[y] < 0:
                    target[y] = i
        return [target[x] for x in groups]


def test_assign_elements():
    solution = Solution()
    assert solution.assignElements([8, 4, 3, 2, 4], [4, 2]) == [0, 0, -1, 1, 0], 'wrong result'
    assert solution.assignElements([2, 3, 5, 7], [5, 3, 3]) == [-1, 1, 0, -1], 'wrong result'
    assert solution.assignElements([10, 21, 30, 41], [2, 1]) == [0, 1, 0, 1], 'wrong result'


if __name__ == '__main__':
    test_assign_elements()
