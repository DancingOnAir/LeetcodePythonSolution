class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        l = 0
        for r, c in enumerate(s):
            if r == 0:
                continue
            if s[r - 1] != c:
                if r - l == k:
                    return True
                l = r
        return len(s) - l == k


def test_has_special_substring():
    solution = Solution()
    assert solution.hasSpecialSubstring("h", 1), 'wrong result'
    assert solution.hasSpecialSubstring("aaabaaa", 3), 'wrong result'
    assert not solution.hasSpecialSubstring("abc", 2), 'wrong result'


if __name__ == '__main__':
    test_has_special_substring()
