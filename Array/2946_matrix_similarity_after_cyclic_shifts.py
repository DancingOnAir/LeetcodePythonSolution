from typing import List
from math import lcm


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for r in mat:
            n = len(r)
            for i in range(n):
                if r[i] != r[(i + k) % n]:
                    return False

        return True

    # math
    def areSimilar1(self, mat: List[List[int]], k: int) -> bool:
        repeats = []
        m, n = len(mat), len(mat[0])
        for r in mat:
            for j, c in enumerate(r):
                if n % (j + 1) == 0:
                    if r[:j+1] * (n // (j + 1)) == r:
                        repeats.append(j + 1)
                        break
        return k % lcm(*repeats) == 0


def test_are_similar():
    solution = Solution()
    assert not solution.areSimilar([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4), 'wrong result'
    assert solution.areSimilar([[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], 2), 'wrong result'
    assert solution.areSimilar([[2, 2], [2, 2]], 3), 'wrong result'


if __name__ == '__main__':
    test_are_similar()
