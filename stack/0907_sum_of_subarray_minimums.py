class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        arr.append(-1)
        res = 0
        stk = [-1]
        for r, x in enumerate(arr):
            while len(stk) > 1 and arr[stk[-1]] >= x:
                i = stk.pop()
                res += arr[i] * (i - stk[-1]) * (r - i)
            stk.append(r)
        return res


def test_sum_subarray_mins():
    solution = Solution()
    assert solution.sumSubarrayMins([3, 1, 2, 4]) == 17, 'wrong result'
    assert solution.sumSubarrayMins([11, 81, 94, 43, 3]) == 444, 'wrong result'


if __name__ == '__main__':
    test_sum_subarray_mins()
