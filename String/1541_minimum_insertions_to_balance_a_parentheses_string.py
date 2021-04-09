class Solution:
    def minInsertions(self, s: str) -> int:
        res = right = 0

        for c in s:
            if c == '(':
                if right % 2:
                    res += 1
                    right -= 1

                right += 2
            elif c == ')':
                right -= 1
                if right < 0:
                    res += 1
                    right += 2

        return res + right

    def minInsertions1(self, s: str) -> int:
        stk = list()
        i = 0
        res = 0
        while i < len(s):
            if s[i] == '(':
                stk.append(s[i])
                i += 1
            elif s[i:i+2] == '))':
                if stk and stk[-1] == '(':
                    stk.pop()
                else:
                    stk.append(s[i:i+2])
                i += 2
            elif s[i] == ')':
                if stk and stk[-1] == '(':
                    stk.pop()
                    res += 1
                else:
                    res += 2
                i += 1
        n = stk.count('(')
        res += n * 2 + (len(stk) - n)
        return res


def test_min_insertions():
    solution = Solution()
    # assert solution.minInsertions('(()))') == 1, 'wrong result'
    # assert solution.minInsertions('())') == 0, 'wrong result'
    assert solution.minInsertions('))())(') == 3, 'wrong result'
    assert solution.minInsertions('((((((') == 12, 'wrong result'
    assert solution.minInsertions(')))))))') == 5, 'wrong result'


if __name__ == '__main__':
    test_min_insertions()
