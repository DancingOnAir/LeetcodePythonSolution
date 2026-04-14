from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        cnt = Counter()
        for r in matrix:
            if r[0]:
                for j in range(len(r)):
                    r[j] ^= 1
            cnt[tuple(r)] += 1
        return max(cnt.values())


def test_max_equal_rows_after_flips():
    solution = Solution()
    assert solution.maxEqualRowsAfterFlips([[0, 1], [1, 1]]) == 1, 'wrong result'
    assert solution.maxEqualRowsAfterFlips([[0, 1], [1, 0]]) == 2, 'wrong result'
    assert solution.maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_equal_rows_after_flips()
