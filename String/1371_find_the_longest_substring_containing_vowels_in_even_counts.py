class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = mark = 0
        memo = {0: -1}
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}

        for i, c in enumerate(s):
            if c in vowels:
                mark ^= 1 << vowels[c]
            if mark not in memo:
                memo[mark] = i
            else:
                res = max(res, i - memo[mark])

        return res

    def findTheLongestSubstring1(self, s: str) -> int:
        res = mask = 0
        memo = {0: -1}

        for i, c in enumerate(s):
            mask ^= (1 << ('aeiou'.find(c) + 1) >> 1)
            memo.setdefault(mask, i)
            res = max(res, i - memo[mask])
        return res


def test_find_the_longest_substring():
    solution = Solution()
    # assert solution.findTheLongestSubstring('eleetminicoworoep') == 13, 'wrong result'
    # assert solution.findTheLongestSubstring('leetcodeisgreat') == 5, 'wrong result'
    assert solution.findTheLongestSubstring('bcbcbc') == 6, 'wrong result'


if __name__ == '__main__':
    test_find_the_longest_substring()
