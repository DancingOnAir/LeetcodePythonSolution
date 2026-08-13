from bisect import bisect_left


class FenwickTree:
    def __init__(self, n: int) -> None:
        self.tree = [0] * (n + 1)

    # a[i]增加1
    def add(self, i: int) -> None:
        t = self.tree
        while i < len(t):
            t[i] += 1
            i += i & -i

    # 计算前缀和 a[1] + a[2] + ... + a[i]
    def pre(self, i: int) -> int:
        t = self.tree
        res = 0
        while i > 0:
            res += t[i]
            i &= i - 1
        return res


class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            # 奇数视为-b, 偶数视为a
            s[i + 1] = s[i] + (a if x % 2 else -b)

        sorted_s = sorted(set(s))
        t = FenwickTree(len(sorted_s) + 1)
        res = 0
        for x in s:
            i = bisect_left(sorted_s, x) + 1
            # 计算在i左边有多少个小于x的数
            res += t.pre(i)
            t.add(i)
        return res


def test_count_ratio_subarrays():
    solution = Solution()
    assert solution.countRatioSubarrays([1, 2, 1, 2], a=3, b=2) == 7, 'wrong result'
    assert solution.countRatioSubarrays([2, 2, 1], a=2, b=1) == 3, 'wrong result'
    assert solution.countRatioSubarrays([2, 2, 2], a=1, b=1) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_ratio_subarrays()
