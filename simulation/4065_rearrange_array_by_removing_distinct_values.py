from collections import Counter


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        res = []
        while cnt:
            res += sorted(cnt)
            cnt -= Counter(cnt.keys())
        return res

    def rearrangeArray1(self, nums: list[int]) -> list[int]:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1

        n = len(nums)
        res = []
        while len(res) < n:
            for x, v in enumerate(cnt):
                if v > 0:
                    res.append(x)
                    cnt[x] -= 1
        return res


def test_rearrange_array():
    solution = Solution()
    assert solution.rearrangeArray([3, 1, 3, 2, 1, 3]) == [1, 2, 3, 1, 3, 3], 'wrong result'
    assert solution.rearrangeArray([7, 7, 4, 4, 4]) == [4, 7, 4, 7, 4], 'wrong result'


if __name__ == '__main__':
    test_rearrange_array()
