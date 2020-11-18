from typing import List


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0] + A + [0]
        stk = []
        res = 0
        for i in range(len(A)):
            while stk and A[i] < A[stk[-1]]:
                cur = stk.pop()
                left = stk[-1]
                right = i
                res += A[cur] * (right - cur) * (cur - left)
            stk.append(i)
        return res % (10 ** 9 + 7)

    def sumSubarrayMins2(self, A: List[int]) -> int:
        res, n, mod = 0, len(A), 10 ** 9 + 7
        left, right, s1, s2 = [0] * n, [0] * n, [], []

        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])

        for i in range(n - 1, -1, -1):
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])

        return sum(l * r * a for l, r, a in zip(left, right, A)) % mod

    def sumSubarrayMins1(self, A: List[int]) -> int:
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

