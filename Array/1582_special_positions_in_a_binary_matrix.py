from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0

        transposed = list(zip(*mat))
        for i in range(len(mat)):
            if mat[i].count(1) == 1:
                try:
                    pos = mat[i].index(1)
                except ValueError:
                    continue

                if transposed[pos].count(1) == 1:
                    res += 1
        return res


def test_num_special():
    solution = Solution()

    mat1 = [[1, 0, 0],
            [0, 0, 1],
            [1, 0, 0]]
    assert solution.numSpecial(mat1) == 1, "wrong result"

    mat2 = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]
    assert solution.numSpecial(mat2) == 3, "wrong result"

    mat3 = [[0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]]
    assert solution.numSpecial(mat3) == 2, "wrong result"

    mat4 = [[0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]]
    assert solution.numSpecial(mat4) == 3, "wrong result"


if __name__ == '__main__':
    test_num_special()
