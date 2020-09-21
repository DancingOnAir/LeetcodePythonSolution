from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        transposed = zip(*matrix)
        for i, row in enumerate(transposed):
            col_max = max(row)
            pos = row.index(col_max)
            if min(matrix[pos]) == col_max:
                res.append(col_max)
        return res


def test_lucky_numbers():
    solution = Solution()

    matrix1 = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    print(solution.luckyNumbers(matrix1))

    matrix2 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    print(solution.luckyNumbers(matrix2))

    matrix3 = [[7, 8], [1, 2]]
    print(solution.luckyNumbers(matrix3))


if __name__ == '__main__':
    test_lucky_numbers()
