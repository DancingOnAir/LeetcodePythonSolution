class Solution:
    # https://leetcode.com/problems/valid-parenthesis-string/solutions/107570/java-c-python-one-pass-count-the-open-parenthesis/
    def checkValidString(self, s: str) -> bool:
        # 未匹配的左括号的个数最小值和最大值
        mn = mx = 0
        for ch in s:
            if ch == '(':
                mn += 1
                mx += 1
            elif ch == ')':
                mn -= 1
                mx -= 1
                if mx < 0:
                    return False
            else:
                # ‘*’改为右括号
                mn -= 1
                # ‘*’改为左括号
                mx += 1
            mn = max(mn, 0)
        return mn == 0

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
