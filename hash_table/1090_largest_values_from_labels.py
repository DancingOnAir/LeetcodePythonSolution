from collections import defaultdict


class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        cnt = defaultdict(int)
        res = 0
        for v, l in sorted(zip(values, labels), reverse=True):
            if cnt[l] < useLimit:
                cnt[l] += 1
                res += v
                numWanted -= 1
                if numWanted == 0:
                    break
        return res


def test_largest_vals_from_labels():
    solution = Solution()
    assert solution.largestValsFromLabels([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1) == 9, 'wrong result'
    assert solution.largestValsFromLabels([5, 4, 3, 2, 1], [1, 3, 3, 3, 2], 3, 2) == 12, 'wrong result'
    assert solution.largestValsFromLabels([9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 1) == 16, 'wrong result'


if __name__ == '__main__':
    test_largest_vals_from_labels()
