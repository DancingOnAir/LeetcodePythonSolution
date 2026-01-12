from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        res = 0
        unsorted = set(range(n - 1))
        for j in range(m):
            if any(strs[i][j] > strs[i + 1][j] for i in unsorted):
                res += 1
            else:
                unsorted -= {i for i in unsorted if strs[i][j] < strs[i + 1][j]}
        return res


def test_min_deletion_size():
    solution = Solution()
    assert solution.minDeletionSize(["ca", "bb", "ac"]) == 1, 'wrong result'
    assert solution.minDeletionSize(["xc", "yb", "za"]) == 0, 'wrong result'
    assert solution.minDeletionSize(["zyx", "wvu", "tsr"]) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_deletion_size()
