class Solution:
    # stack
    def minimumDeletions(self, s: str) -> int:
        res = 0
        stk = []
        for c in s:
            if stk and stk[-1] == 'b' and c == 'a':
                stk.pop()
                res += 1
            else:
                stk.append(c)

        return res

    # dp
    def minimumDeletions3(self, s: str) -> int:
        cnt_b = 0
        dp = [0]
        for c in s:
            if c == 'b':
                cnt_b += 1
                dp.append(dp[-1])
            else:
                dp.append(min(cnt_b, dp[-1] + 1))
        return dp[-1]

    # two passes with space O(1)
    def minimumDeletions2(self, s: str) -> int:
        cnt_a, cnt_b, res = s.count('a'), 0, len(s)
        for c in s:
            if c == 'b':
                res = min(res, cnt_a + cnt_b)
                cnt_b += 1
            else:
                cnt_a -= 1
        return min(res, cnt_b)

    # two passes
    def minimumDeletions1(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0

        pre_sum_b = [0] * n
        for i in range(1, n):
            pre_sum_b[i] = pre_sum_b[i - 1] + (1 if s[i - 1] == 'b' else 0)

        suf_sum_a = [0] * n
        for i in range(n - 2, -1, -1):
            suf_sum_a[i] = suf_sum_a[i + 1] + (1 if s[i + 1] == 'a' else 0)

        res = float('inf')
        for i in range(n):
            res = min(res, pre_sum_b[i] + suf_sum_a[i])
        return res


def test_minimum_deletions():
    solution = Solution()
    assert solution.minimumDeletions('aababbab') == 2, 'wrong result'
    assert solution.minimumDeletions('bbaaaaabb') == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_deletions()
