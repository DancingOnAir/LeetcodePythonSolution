from typing import List
from collections import defaultdict


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        m = defaultdict(bool)
        for x, y in dig:
            m[(x, y)] = True

        res = 0
        for a in artifacts:
            if all(m[(i, j)] for i in range(a[0], a[2] + 1) for j in range(a[1], a[3] + 1)):
                res += 1
        return res


def test_dig_artifacts():
    solution = Solution()
    assert solution.digArtifacts(2, [[0, 0, 0, 0], [0, 1, 1, 1]], [[0, 0], [0, 1]]) == 1, 'wrong result'
    assert solution.digArtifacts(2, [[0, 0, 0, 0], [0, 1, 1, 1]], [[0, 0], [0, 1], [1, 1]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_dig_artifacts()
