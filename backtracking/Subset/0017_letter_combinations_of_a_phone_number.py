from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        alphabet = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = list()
        path = [''] * n

        def dfs(i):
            if i == n:
                res.append(''.join(path))
                return

            for c in alphabet[int(digits[i])]:
                path[i] = c
                dfs(i + 1)

        dfs(0)
        return res


def test_letter_combinations():
    solution = Solution()
    assert solution.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], 'wrong result'
    assert solution.letterCombinations("") == [], 'wrong result'
    assert solution.letterCombinations("2") == ["a", "b", "c"], 'wrong result'


if __name__ == '__main__':
    test_letter_combinations()
