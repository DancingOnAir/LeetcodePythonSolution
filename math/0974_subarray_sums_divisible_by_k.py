from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        res = tot = 0
        for i, x in enumerate(nums):
            cnt[tot] += 1
            tot = (tot + x) % k
            res += cnt[tot]
        return res


def test_subarrays_div_by_k():
    solution = Solution()
    assert solution.subarraysDivByK([4, 5, 0, -2, -3, 1], k=5) == 7, 'wrong result'
    assert solution.subarraysDivByK([5], k=9) == 0, 'wrong result'


if __name__ == '__main__':
    test_subarrays_div_by_k()
