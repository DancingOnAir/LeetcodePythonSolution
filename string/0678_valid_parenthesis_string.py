class Solution:
    # https://leetcode.com/problems/valid-parenthesis-string/solutions/107570/java-c-python-one-pass-count-the-open-parenthesis/
    def checkValidString(self, s: str) -> bool:
        cmin, cmax = 0, 0
        for ch in s:
            if ch == '(':
                cmin += 1
                cmax += 1
            elif ch == ')':
                cmin = max(cmin - 1, 0)
                cmax -= 1
            else:
                cmin = max(cmin - 1, 0)
                cmax += 1

            if cmax < 0:
                return False
        return cmin == 0

    # TLE
    def checkValidString1(self, s: str) -> bool:
        def helper(bal, x):
            if x == '*':
                return True

            for i, c in enumerate(x):
                if c == '(':
                    bal += 1
                elif c == ')':
                    bal -= 1
                    if bal < 0:
                        return False
                else:
                    return any(helper(bal, val + x[i+1:]) for val in ['(', ')', ''])
            return bal == 0

        return helper(0, s)


def test_check_valid_string():
    solution = Solution()
    assert solution.checkValidString("()"), 'wrong result'
    assert solution.checkValidString("(*)"), 'wrong result'
    assert solution.checkValidString("(*))"), 'wrong result'


if __name__ == '__main__':
    test_check_valid_string()
