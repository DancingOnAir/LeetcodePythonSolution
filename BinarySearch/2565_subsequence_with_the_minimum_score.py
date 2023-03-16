from typing import List


class Solution:
    # https://leetcode.com/problems/subsequence-with-the-minimum-score/solutions/3174009/c-clean-explained/
    def minimumScore(self, s: str, t: str) -> int:
        l1, l2 = len(s), len(t)
        pre = [-1] * l2
        j = 0
        for i, c in enumerate(s):
            if j >= l2:
                break

            if t[j] == c:
                pre[j] = i
                j += 1

        suf = [-1] * l2
        j = l2 - 1
        for i in range(l1 - 1, -1, -1):
            if j < 0:
                break
            if s[i] == t[j]:
                suf[j] = i
                j -= 1

        res = l2
        for i in range(l2):
            if pre[i] != -1:
                res = min(res, l2 - i - 1)
            if suf[i] != -1:
                res = min(res, i)

        if suf[-1] == -1:
            return res

        for i in range(l2 - 1):
            if pre[i] != -1:
                if pre[i] >= suf[l2 - 1]:
                    break
                lo, hi = i + 1, l2 - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if pre[i] < suf[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                res = min(res, lo - i - 1)
        return res

    # https://leetcode.cn/problems/subsequence-with-the-minimum-score/solution/qian-hou-zhui-fen-jie-san-zhi-zhen-pytho-6cmr/
    def minimumScore1(self, s: str, t: str) -> int:
        l1, l2 = len(s), len(t)
        suf = [l2] * (l1 + 1)
        j = l2 - 1
        for i in range(l1 - 1, -1, -1):
            if j >= 0 and s[i] == t[j]:
                j -= 1
            suf[i] = j + 1

        res = suf[0]
        if res == 0:
            return 0

        j = 0
        for i, v in enumerate(s):
            if t[j] == v:
                # 这里suf[i + 1] - j - 1表示最小后缀位置减去最大前置的位置
                res = min(res, suf[i + 1] - j - 1)
                j += 1
        return res


def test_minimum_score():
    solution = Solution()
    assert solution.minimumScore("abecdebe", "eaebceae") == 6, 'wrong result'
    assert solution.minimumScore("abacaba", "bzaa") == 1, 'wrong result'
    assert solution.minimumScore("cde", "xyz") == 3, 'wrong result'


if __name__ == '__main__':
    test_minimum_score()
