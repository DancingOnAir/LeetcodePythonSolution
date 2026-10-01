from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        res = tot = 0
        for x in nums:
            tot += x
            res += cnt[tot - k]
            cnt[tot] += 1
        return res


def test_subarray_sum():
    solution = Solution()
    assert solution.subarraySum([1, 1, 1], k=2) == 2, 'wrong result'
    assert solution.subarraySum([1, 2, 3], k=3) == 2, 'wrong result'


if __name__ == '__main__':
    test_subarray_sum()
