from typing import List


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        right = [n] * n
        stk = list()
        for i in range(n):
            while stk and A[stk[-1]] >= A[i]:
                right[stk.pop()] = i
            stk.append(i)

        left = [-1] * n
        stk.clear()
        for i in range(n - 1, -1, -1):
            while stk and A[stk[-1]] > A[i]:
                left[stk.pop()] = i
            stk.append(i)

        res = 0
        for i in range(n):
            res += A[i] * (i - left[i]) * (right[i] - i)
        return res % (10 ** 9 + 7)

    def sumSubarrayMins1(self, A: List[int]) -> int:
        A = [0] + A + [0]
        res = 0
        stk = list()
        for i in range(len(A)):
            while stk and A[i] < A[stk[-1]]:
                cur = stk.pop()
                left = stk[-1]
                res += A[cur] * (cur - left) * (i - cur)
            stk.append(i)
        return res % (10 ** 9 + 7)


def test_sum_subarray_mins():
    solution = Solution()
    assert solution.sumSubarrayMins([3, 1, 2, 4]) == 17, 'wrong result'
    assert solution.sumSubarrayMins([11, 81, 94, 43, 3]) == 444, 'wrong result'


if __name__ == '__main__':
    test_sum_subarray_mins()
