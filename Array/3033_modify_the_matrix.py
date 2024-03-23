from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        c = 0
        for col in zip(*matrix):
            mx = max(col)
            for r, val in enumerate(col):
                if val == -1:
                    matrix[r][c] = mx
            c += 1
        return matrix


def test_modified_matrix():
    solution = Solution()
    assert solution.modifiedMatrix([[1, 2, -1], [4, -1, 6], [7, 8, 9]]) == [[1, 2, 9], [4, 8, 6],
                                                                            [7, 8, 9]], 'wrong result'
    assert solution.modifiedMatrix([[3, -1], [5, 2]]) == [[3, 2], [5, 2]], 'wrong result'


if __name__ == '__main__':
    test_modified_matrix()
