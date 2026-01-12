from typing import List


class Solution:
    # backtracking + pruning
    # time complex O(n x 2^n)
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return not cnt

        res = list()
        def helper(s, start, left, right):
            if left == 0 and right == 0:
                if isValid(s):
                    res.append(s)
                return

            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                # 如果剩余的字符无法满足去掉的数量要求
                if left + right > len(s) - i:
                    break
                # 尝试去掉一个左括号
                if left > 0 and s[i] == '(':
                    helper(s[:i] + s[i+1:], i, left - 1, right)
                # 尝试去掉一个右括号
                if right > 0 and s[i] == ')':
                    helper(s[:i] + s[i+1:], i, left, right - 1)

        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1

        helper(s, 0, left, right)
        return res

    # breadth first search
    # time complex O(n x 2^n)
    def removeInvalidParentheses1(self, s: str) -> List[str]:
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

