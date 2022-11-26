from typing import List


class Solution:
    # TLE
    def totalStrength(self, strength: List[int]) -> int:
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
