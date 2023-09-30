class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return all((s1[i] == s2[i] and s1[i + 2] == s2[i + 2]) or (s1[i] == s2[i + 2] and s1[i + 2] == s2[i]) for i in range(2))


def test_can_be_equal():
    solution = Solution()
    assert solution.canBeEqual("abcd", "cdab"), 'wrong result'
    assert not solution.canBeEqual("abcd", "dacb"), 'wrong result'


if __name__ == '__main__':
    test_can_be_equal()
