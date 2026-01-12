class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = list()
        for c in expression:
            if c == ')':
                seen = set()
                while stk[-1] != '(':
                    seen.add(stk.pop())
                stk.pop()
                op = stk.pop()
                stk.append(all(seen) if op == '&' else any(seen) if op == '|' else not seen.pop())
            elif c != ',':
                stk.append(True if c == 't' else False if c == 'f' else c)

        return stk.pop()

    def parseBoolExpr2(self, expression: str, t=True, f=False) -> bool:
        return eval(expression.replace('!', 'not &').replace('|(', 'any([').replace('&(', 'all([').replace(')', '])'))

    def parseBoolExpr1(self, expression: str) -> bool:
        def parse_helper(expr: str) -> bool:
            if expr[0] == 'f':
                return False
            elif expr[0] == 't':
                return True
            else:
                if expr[0] == '!':
                    return not parse_helper(expr[2: -1])
                if expr[0] == '|' or expr[0] == '&':
                    sub_expr = list()
                    cur = expr[2: -1]
                    cnt = i = j = 0
                    while j < len(cur):
                        if cur[j] == ',' and cnt == 0:
                            sub_expr.append(cur[i:j])
                            i = j + 1
                        elif cur[j] == '(':
                            cnt += 1
                        elif cur[j] == ')':
                            cnt -= 1
                        j += 1
                    sub_expr.append(cur[i:])

                    if expr[0] == '|':
                        return any(parse_helper(s) for s in sub_expr)
                    elif expr[0] == '&':
                        return all(parse_helper(s) for s in sub_expr)

        return parse_helper(expression)


def test_parse_bool_expr():
    solution = Solution()

    assert solution.parseBoolExpr('&(t,t,t)'), 'wrong result'
    assert solution.parseBoolExpr('!(f)'), 'wrong result'
    assert solution.parseBoolExpr('|(f,t)'), 'wrong result'
    assert not solution.parseBoolExpr('&(t,f)'), 'wrong result'
    assert not solution.parseBoolExpr('|(&(t,f,t),!(t))'), 'wrong result'


if __name__ == '__main__':
    test_parse_bool_expr()
