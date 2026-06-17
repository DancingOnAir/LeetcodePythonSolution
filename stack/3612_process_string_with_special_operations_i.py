class Solution:
    def processStr(self, s: str) -> str:
        res = ''
        for c in s:
            if c == '#':
                res += res
            elif c == '*':
                if res:
                    res = res[:-1]
            elif c == '%':
                res = res[::-1]
            else:
                res += c
        return res

    def processStr1(self, s: str) -> str:
        stk = []
        for c in s:
            if c == '#':
                stk *= 2
            elif c == '*':
                if stk:
                    stk.pop()
            elif c == '%':
                stk.reverse()
            else:
                stk.append(c)
        return ''.join(stk)


def test_process_str():
    solution = Solution()
    assert solution.processStr("*%") == "", 'wrong result'
    assert solution.processStr("a#b%*") == "ba", 'wrong result'
    assert solution.processStr("z*#") == "", 'wrong result'


if __name__ == '__main__':
    test_process_str()
