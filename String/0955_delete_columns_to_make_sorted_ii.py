from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        for i in range(m):
            cur = [s[i] for s in strs]
            if sorted(cur) == cur:
                return i
        return n


def test_min_deletion_size():
    solution = Solution()
    assert solution.minDeletionSize(["ca", "bb", "ac"]) == 1, 'wrong result'
    assert solution.minDeletionSize(["xc", "yb", "za"]) == 0, 'wrong result'
    assert solution.minDeletionSize(["zyx", "wvu", "tsr"]) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_deletion_size()
