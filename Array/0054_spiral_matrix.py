from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


def test_spiral_order():
    solution = Solution()

    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    print(solution.spiralOrder(matrix1))

    matrix2 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]]
    print(solution.spiralOrder(matrix2))


if __name__ == '__main__':
    test_spiral_order()
