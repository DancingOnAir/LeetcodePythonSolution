from typing import List


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        mi, mx = float('-inf'), float('inf')
        for x, (u, v) in zip(original, bounds):
            d = x - original[0]
            mi = max(mi, u - d)
            mx = min(mx, v - d)
        return max(mx - mi + 1, 0)


def test_count_arrays():
    solution = Solution()
    assert solution.countArrays([1, 2, 3, 4], bounds=[[1, 2], [2, 3], [3, 4], [4, 5]]) == 2, 'wrong result'
    assert solution.countArrays([1, 2, 3, 4], bounds=[[1, 10], [2, 9], [3, 8], [4, 7]]) == 4, 'wrong result'
    assert solution.countArrays([1, 2, 1, 2], bounds=[[1, 1], [2, 3], [3, 3], [2, 3]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_arrays()
