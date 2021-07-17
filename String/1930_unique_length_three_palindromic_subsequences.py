class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        cnt = set()
        chars = set(s)

        for c in chars:
            lo, hi = 0, len(s) - 1
            while lo < hi:
                if s[lo] != c:
                    lo += 1
                elif s[hi] != c:
                    hi -= 1
                else:
                    for i in range(lo + 1, hi):
                        cur = s[lo] + s[i] + s[hi]
                        cnt.add(cur)
                    break
        return len(cnt)


def test_count_palindromic_subsequence():
    solution = Solution()
    assert solution.countPalindromicSubsequence("aabca") == 3, 'wrong result'
    assert solution.countPalindromicSubsequence("adc") == 0, 'wrong result'
    assert solution.countPalindromicSubsequence("bbcbaba") == 4, 'wrong result'


if __name__ == '__main__':
    test_count_palindromic_subsequence()
