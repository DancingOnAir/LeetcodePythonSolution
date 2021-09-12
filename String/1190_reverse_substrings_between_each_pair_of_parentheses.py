class Solution:
    def reverseParentheses(self, s: str) -> str:
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
