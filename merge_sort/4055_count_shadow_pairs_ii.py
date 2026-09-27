from bisect import bisect_left


class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        def helper(arr: list[int], low: int, high: int) -> None:
            if low == high or len(arr) < 2:
                return
            nonlocal res
            mid = (low + high) // 2
            low_stk  = []
            high_stk = []
            b = []
            c = []
            for i, x in enumerate(arr):
                if x <= mid:
                    while low_stk and arr[low_stk[-1]] < x:
                        low_stk.pop()
                    low_stk.append(i)
                    b.append(x)
                else:
                    while high_stk and arr[high_stk[-1]] >= x:
                        high_stk.pop()
                    res += len(low_stk)
                    if high_stk:
                        res -= bisect_left(low_stk, high_stk[-1])
                    high_stk.append(i)
                    c.append(x)
            helper(b, low, mid)
            helper(c, mid + 1, high)
        sorted_nums = sorted(set(nums))
        for i, x in enumerate(nums):
            nums[i] = bisect_left(sorted_nums, x)

        res = 0
        helper(nums, 0, len(sorted_nums) - 1)
        return res


def test_shadow_pairs():
    solution = Solution()
    assert solution.shadowPairs([3, 1, 4, 2, 5]) == 5, 'wrong result'
    assert solution.shadowPairs([6, 7, 8, 9]) == 3, 'wrong result'


if __name__ == '__main__':
    test_shadow_pairs()
