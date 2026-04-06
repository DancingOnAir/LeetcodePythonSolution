class Solution:
    # n^3
    def countQuadruplets(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        cnt = [0] * 301
        for c in range(n - 2, 2, -1):
            cnt[nums[c + 1]] += 1
            for a in range(n - 3):
                for b in range(a + 1, n - 2):
                    res += cnt[nums[a] + nums[b] + nums[c]]
        return res

    # n^4
    def countQuadruplets(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            res += 1
        return res


def test_count_quadruplets():
    solution = Solution()
    assert solution.countQuadruplets([1, 2, 3, 6]) == 1, 'wrong result'
    assert solution.countQuadruplets([3, 3, 6, 4, 5]) == 0, 'wrong result'
    assert solution.countQuadruplets([1, 1, 1, 3, 5]) == 4, 'wrong result'


if __name__ == '__main__':
    test_count_quadruplets()
