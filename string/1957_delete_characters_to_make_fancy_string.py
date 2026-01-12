class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        pre = ''
        cnt = 0

        for c in s:
            if c == pre:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                res += c
            pre = c
        return res

    def makeFancyString1(self, s: str) -> str:
        stk = list()
        for c in s:
            if len(stk) > 1 and c == stk[-1] == stk[-2]:
                continue
            else:
                stk.append(c)
        return ''.join(stk)


def test_make_fancy_string():
    solution = Solution()

    assert solution.makeFancyString("leeetcode") == "leetcode", 'wrong result'
    assert solution.makeFancyString("aaabaaaa") == "aabaa", 'wrong result'
    assert solution.makeFancyString("aab") == "aab", 'wrong result'


if __name__ == '__main__':
    test_make_fancy_string()
