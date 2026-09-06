from math import gcd


class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(-1, n):
            arr = [nums[j] for j in range(n) if j != i]
            m = len(arr)
            if m < 2:
                continue

            prefix_gcd = [arr[0]]
            for j in range(1, m):
                prefix_gcd.append(gcd(prefix_gcd[-1], arr[j]))

            suffix_gcd = [arr[-1]]
            for j in range(m - 2, -1, -1):
                suffix_gcd.append(gcd(suffix_gcd[-1], arr[j]))
            suffix_gcd.reverse()

            cur = 0
            for j in range(m - 1):
                if prefix_gcd[j] == suffix_gcd[j + 1]:
                    cur += 1
            res = max(res, cur)
        return res


def test_max_valid_splits():
    solution = Solution()
    assert solution.maxValidSplits([10, 30, 15, 10]) == 2, 'wrong result'
    assert solution.maxValidSplits([2, 10, 14]) == 1, 'wrong result'
    assert solution.maxValidSplits([2, 4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_valid_splits()
