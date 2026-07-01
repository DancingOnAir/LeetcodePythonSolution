class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        n = len(arr)
        cnt = [0] * (n + 1)
        for i, x in enumerate(arr):
            cnt[min(x, n)] += 1

        res = 1
        for x in range(1, n + 1):
            res = min(res + cnt[x], x)
        return res

    def maximumElementAfterDecrementingAndRearranging1(self, arr: list[int]) -> int:
        arr.sort()
        res = 0
        for x in arr:
            res = min(res + 1, x)
        return res


def test_maximum_element_after_decreasing_and_rearranging():
    solution = Solution()
    assert solution.maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]) == 2, 'wrong result'
    assert solution.maximumElementAfterDecrementingAndRearranging([100, 1, 1000]) == 3, 'wrong result'
    assert solution.maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]) == 5, 'wrong result'


if __name__ == '__main__':
    test_maximum_element_after_decreasing_and_rearranging()
