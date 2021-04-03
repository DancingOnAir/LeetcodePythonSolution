# class Solution:
#     def findTheLongestSubstring(self, s: str) -> int:
#         res = mask = 0
#         memo = [-1] * (1 << 5)
#         memo[0] = 0
#
#         for i, c in enumerate(s):
#             if c == 'a':
#                 mask ^= 1 << 0
#             elif c == 'e':
#                 mask ^= 1 << 1
#             elif c == 'i':
#                 mask ^= 1 << 2
#             elif c == 'o':
#                 mask ^= 1 << 3
#             elif c == 'eu':
#                 mask ^= 1 << 4
#
#             if ~memo[mask]:
#                 res = max(res, i + 1 - memo[mask])
#             else:
#                 memo[mask] = i + 1
#         return res

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
