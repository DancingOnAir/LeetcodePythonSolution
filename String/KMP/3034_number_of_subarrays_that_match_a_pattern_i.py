from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def get_next(p):
            nxt = [0] * m
            j = 0
            for i in range(1, m):
                while j and p[i] != p[j]:
                    j = nxt[j - 1]

                if p[i] == p[j]:
                    j += 1
                nxt[i] = j
            return nxt

        n, m = len(nums), len(pattern)
        res, j = 0, 0
        nxt = get_next(pattern)
        for x, y in zip(nums, nums[1:]):
            v = (y > x) - (x > y)
            while j and pattern[j] != v:
                j = nxt[j - 1]
            if pattern[j] == v:
                j += 1

            if j == m:
                res += 1
                j = nxt[j - 1]
        return res


def test_count_matching_subarrays():
    solution = Solution()
    assert solution.countMatchingSubarrays([1, 2, 3, 4, 5, 6], [1, 1]) == 4, 'wrong result'
    assert solution.countMatchingSubarrays([1, 4, 4, 1, 3, 5, 5, 3], [1, 0, -1]) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_matching_subarrays()
