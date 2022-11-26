from typing import List
from itertools import  accumulate


class Solution:
    # one pass
    def totalStrength(self, strength: List[int]) -> int:
        pass

    # https://leetcode.com/problems/sum-of-total-strength-of-wizards/solutions/2061985/java-c-python-one-pass-solution/
    # for each strength[i] as minimum, calculate sum
    def totalStrength2(self, strength: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(strength)

        # next small on the right
        right = [n] * n
        stk = list()
        for i in range(n):
            while stk and strength[stk[-1]] > strength[i]:
                right[stk.pop()] = i
            stk.append(i)

        # next small on the left
        left = [-1] * n
        stk = list()
        for i in range(n - 1, -1, -1):
            while stk and strength[stk[-1]] >= strength[i]:
                left[stk.pop()] = i
            stk.append(i)
        # 注意这里
        pre_sum = list(accumulate(accumulate(strength), initial=0))
        res = 0
        for i in range(n):
            l, r = left[i], right[i]
            l_pre_sum = pre_sum[i] - pre_sum[max(l, 0)]
            r_pre_sum = pre_sum[r] - pre_sum[i]
            ln, rn = i - l, r - i
            res += strength[i] * (r_pre_sum * ln - l_pre_sum * rn)
            res %= mod
        return res

    # TLE
    def totalStrength1(self, strength: List[int]) -> int:
        n = len(strength)
        pre_sum = [0]
        for s in strength:
            pre_sum.append(pre_sum[-1] + s)

        res = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            stk = list()
            for j in range(i, n):
                while stk and strength[stk[-1]] > strength[j]:
                    stk.pop()
                stk.append(j)
                res += strength[stk[0]] * (pre_sum[j + 1] - pre_sum[i])
                res %= mod
        return res


def test_total_strength():
    solution = Solution()
    assert solution.totalStrength([1, 3, 1, 2]) == 44, 'wrong result'
    assert solution.totalStrength([5, 4, 6]) == 213, 'wrong result'


if __name__ == '__main__':
    test_total_strength()
