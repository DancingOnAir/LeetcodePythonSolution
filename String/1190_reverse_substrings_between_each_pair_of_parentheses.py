class Solution:
    # straight forward
    def reverseParentheses(self, s: str) -> str:
        stk = [[]]
        for c in s:
            if c == '(':
                stk.append([])
            elif c == ')':
                end = stk.pop()
                stk[-1].extend(reversed(end))
            else:
                stk[-1].append(c)
        return ''.join(stk.pop())

    # wormholes
    def reverseParentheses2(self, s: str) -> str:
        opened_bracket = list()
        pair = dict()
        for i, c in enumerate(s):
            if c == '(':
                opened_bracket.append(i)
            elif c == ')':
                j = opened_bracket.pop()
                pair[i] = j
                pair[j] = i

        res = list()
        i = 0
        d = 1
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return ''.join(res)

    # stack
    def reverseParentheses1(self, s: str) -> str:
        stk = list()
        for c in s:
            if c == ')':
                cur = list()
                while stk[-1] != '(':
                    cur.append(stk.pop())
                stk.pop()
                stk += cur
            else:
                stk.append(c)
        return ''.join(stk)


def test_reverse_parentheses():
    solution = Solution()

    assert solution.reverseParentheses("(abcd)") == "dcba", 'wrong result'
    assert solution.reverseParentheses("(u(love)i)") == "iloveu", 'wrong result'
    assert solution.reverseParentheses("(ed(et(oc))el)") == "leetcode", 'wrong result'
    assert solution.reverseParentheses("a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq", 'wrong result'


if __name__ == '__main__':
    test_reverse_parentheses()
