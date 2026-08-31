from collections import defaultdict


MX = 100001
prime_factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not prime_factors[i]:
        for j in range(i, MX, i):
            prime_factors[j].append(i)

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        res = 0
        l = 0
        cnt = defaultdict(int)
        for r, x in enumerate(nums):
            for p in prime_factors[x]:
                cnt[p] += 1

            while len(cnt) > k:
                for p in prime_factors[nums[l]]:
                    if cnt[p] > 1:
                        cnt[p] -= 1
                    else:
                        del cnt[p]
                l += 1
            res = max(res, r - l + 1)
        return res


def test_longest_subarray():
    solution = Solution()
    assert solution.longestSubarray([7, 6, 10, 12, 11], k=3) == 3, 'wrong result'
    assert solution.longestSubarray([4, 6, 9, 18], k=4) == 4, 'wrong result'
    assert solution.longestSubarray([6, 10, 15], k=2) == 1, 'wrong result'


if __name__ == '__main__':
    test_longest_subarray()
