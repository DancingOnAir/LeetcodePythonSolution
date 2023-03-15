from typing import List


class Solution:
    # https://leetcode.cn/problems/subsequence-with-the-minimum-score/solution/qian-hou-zhui-fen-jie-san-zhi-zhen-pytho-6cmr/
    def minimumScore(self, s: str, t: str) -> int:
        l1, l2 = len(s), len(t)
        suf = [l2] * (l1 + 1)
        j = l2 - 1
        for i in range(l1 - 1, -1, -1):
            if s[i] == t[j]:
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
    assert solution.minimumScore("abacaba", "bzaa") == 1, 'wrong result'
    assert solution.minimumScore("cde", "xyz") == 3, 'wrong result'


if __name__ == '__main__':
    test_minimum_score()
