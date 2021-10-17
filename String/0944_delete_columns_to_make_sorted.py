from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*strs))

    def minDeletionSize1(self, strs: List[str]) -> int:
        res = 0
        for col in zip(*strs):
            for i in range(1, len(col)):
                if col[i - 1] > col[i]:
                    res += 1
                    break
        return res


def test_min_deletion_size():
    solution = Solution()

    assert solution.minDeletionSize(["cba", "daf", "ghi"]) == 1, 'wrong result'
    assert solution.minDeletionSize(["a", "b"]) == 0, 'wrong result'
    assert solution.minDeletionSize(["zyx", "wvu", "tsr"]) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_deletion_size()
