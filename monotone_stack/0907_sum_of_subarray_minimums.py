from typing import List


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stk = [-1]
        dp = [0] * (len(A) + 1)
        res = 0
        mod = 1e9 + 7
        for i in range(len(A)):
            while stk[-1] != -1 and A[stk[-1]] >= A[i]:
                stk.pop()

            dp[i + 1] = (dp[stk[-1] + 1] + (i - stk[-1]) * A[i]) % mod
            res = (res + dp[i + 1]) % mod
            stk.append(i)

        return int(res)


def test_sum_subarray_mins():
    solution = Solution()

    A1 = [3, 1, 2, 4]
    print(solution.sumSubarrayMins(A1))


if __name__ == '__main__':
    test_sum_subarray_mins()

