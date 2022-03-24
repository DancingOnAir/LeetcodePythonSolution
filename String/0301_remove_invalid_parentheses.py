from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return not cnt

        currentLevel = {s}
        while True:
            res = list(filter(isValid, currentLevel))
            if res:
                return res

            nextLevel = set()
            for ss in currentLevel:
                for i, ch in enumerate(ss):
                    if i > 0 and ch == ss[i - 1]:
                        continue
                    if ch in '()':
                        # if the substring is valid parentheses that means it remove the minimum number of invalid
                        # parentheses, so do not need to check next level substrings.
                        nextLevel.add(ss[:i] + ss[i+1:])
            currentLevel = nextLevel


def test_remove_invalid_parentheses():
    solution = Solution()

    assert solution.removeInvalidParentheses("()())()") == ["(())()", "()()()"], 'wrong result'
    assert solution.removeInvalidParentheses("(a)())()") == ["(a())()", "(a)()()"], 'wrong result'
    assert solution.removeInvalidParentheses(")(") == [""], 'wrong result'


if __name__ == '__main__':
    test_remove_invalid_parentheses()

