from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        res = 0
        for i, (_, y0) in enumerate(points):
            max_y = float('-inf')
            for _, y1 in points[i + 1:]:
                if max_y < y1 <= y0:
                    res += 1
                    max_y = y1
        return res


def test_number_of_pairs():
    solution = Solution()
    assert solution.numberOfPairs([[0, 1], [1, 3], [6, 1]]) == 2, 'wrong result'
    assert solution.numberOfPairs([[1, 1], [2, 2], [3, 3]]) == 0, 'wrong result'
    assert solution.numberOfPairs([[6, 2], [4, 4], [2, 6]]) == 2, 'wrong result'
    assert solution.numberOfPairs([[3, 1], [1, 3], [1, 1]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_number_of_pairs()
