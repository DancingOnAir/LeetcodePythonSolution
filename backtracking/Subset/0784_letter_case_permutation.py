from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        if n == 0:
            return []

        res = list()
        path = [''] * n

        def dfs(i):
            if i == n:
                res.append(''.join(path))
                return

            path[i] = s[i]
            dfs(i + 1)
            if s[i].isalpha():
                path[i] = s[i].swapcase()
                dfs(i + 1)
        dfs(0)
        return res


def test_letter_case_permutation():
    solution = Solution()
    assert solution.letterCasePermutation("a1b2") == ["a1b2", "a1B2", "A1b2", "A1B2"], 'wrong result'
    assert solution.letterCasePermutation("3z4") == ["3z4", "3Z4"], 'wrong result'


if __name__ == '__main__':
    test_letter_case_permutation()
