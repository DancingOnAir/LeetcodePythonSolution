from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s: str):
            count = 0
            for c in s:
                count += (c == '(') - (c == ')')
                if count < 0: return False
            return not count
        level = {s}
        while True:
            valid = set(filter(is_valid, level))
            if valid:
                return valid
            level = {sub[:i] + sub[i+1:]
                     for sub in level
                     for i in range(len(sub)) if sub[i] in '()'}


def test_remove_invalid_parentheses():
    solution = Solution()

    assert solution.removeInvalidParentheses("()())()") == ["(())()", "()()()"], 'wrong result'
    assert solution.removeInvalidParentheses("(a)())()") == ["(a())()", "(a)()()"], 'wrong result'
    assert solution.removeInvalidParentheses(")(") == [""], 'wrong result'


if __name__ == '__main__':
    test_remove_invalid_parentheses()

