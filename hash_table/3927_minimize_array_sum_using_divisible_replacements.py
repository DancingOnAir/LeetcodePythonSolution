from collections import Counter


class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        res = 0
        ma = max(cnt)
        for x in sorted(cnt):
            if cnt[x] == 0:
                continue
            for y in range(x, ma + 1, x):
                if cnt[y]:
                    res += x * cnt[y]
                    cnt[y] = 0
        return res

    # TLM
    def minArraySum1(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        sorted_key = sorted(cnt.keys())
        n = len(sorted_key)

        seen = set()
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if sorted_key[j] not in seen and sorted_key[j] % sorted_key[i] == 0:
                    seen.add(sorted_key[j])
                    res += sorted_key[i] * cnt[sorted_key[j]]
            if sorted_key[i] not in seen:
                seen.add(sorted_key[i])
                res += sorted_key[i] * cnt[sorted_key[i]]
        return res


def test_min_array_sum():
    solution = Solution()
    assert solution.minArraySum([3, 6, 2]) == 7, 'wrong result'
    assert solution.minArraySum([4, 2, 8, 3]) == 9, 'wrong result'
    assert solution.minArraySum([7, 5, 9]) == 21, 'wrong result'


if __name__ == '__main__':
    test_min_array_sum()
