from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l * l for _, _, l in squares)

        def check(y):
            area = 0
            for _, yi, l in squares:
                area += l * min(max(y - yi, 0), l)
            return area * 2 >= total_area

        mx_y = max(y + l for _, y, l in squares)
        left, right = 0, mx_y
        for i in range(len(bin(100000 * mx_y))):
            mid = (left + right) / 2
            if check(mid):
                right = mid
            else:
                left = mid
        return (left + right) / 2


def test_separate_squares():
    solution = Solution()
    assert abs(solution.separateSquares([[0, 0, 1], [2, 2, 1]]) - 1.00000) <= 10 ** (-5), 'wrong result'
    assert abs(solution.separateSquares([[0, 0, 2], [1, 1, 1]]) - 1.16667) <= 10 ** (-5), 'wrong result'


if __name__ == '__main__':
    test_separate_squares()
