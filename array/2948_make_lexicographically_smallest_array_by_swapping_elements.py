from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        p = sorted(zip(nums, range(n)))
        res = [0] * n
        i = 0
        while i < n:
            start = i
            i += 1
            while i < n and p[i][0] - p[i - 1][0] <= limit:
                i += 1
            ss = p[start: i]
            ss_idx = sorted(j for _, j in ss)
            for k, (x, _) in zip(ss_idx, ss):
                res[k] = x
        return res


def test_lexicographically_smallest_array():
    solution = Solution()
    assert solution.lexicographicallySmallestArray([1, 5, 3, 9, 8], 2) == [1, 3, 5, 8, 9], 'wrong result'
    assert solution.lexicographicallySmallestArray([1, 7, 6, 18, 2, 1], 3) == [1, 6, 7, 18, 1, 2], 'wrong result'
    assert solution.lexicographicallySmallestArray([1, 7, 28, 19, 10], 3) == [1, 7, 28, 19, 10], 'wrong result'


if __name__ == '__main__':
    test_lexicographically_smallest_array()
