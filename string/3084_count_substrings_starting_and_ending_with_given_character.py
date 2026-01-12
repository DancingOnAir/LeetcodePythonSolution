class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n = s.count(c)
        return (1 + n) * n // 2


def test_count_substrings():
    solution = Solution()
    assert solution.countSubstrings("abada", "a") == 6, 'wrong result'
    assert solution.countSubstrings("zzz", "z") == 6, 'wrong result'


if __name__ == '__main__':
    test_count_substrings()
