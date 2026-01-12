class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return {s1[0], s1[2]} == {s2[0], s2[2]} and {s1[1], s1[3]} == {s2[1], s2[3]}

    def canBeEqual1(self, s1: str, s2: str) -> bool:
        return all({s1[i], s1[i + 2]} == {s2[i], s2[i + 2]} for i in range(2))


def test_can_be_equal():
    solution = Solution()
    assert solution.canBeEqual("abcd", "cdab"), 'wrong result'
    assert not solution.canBeEqual("abcd", "dacb"), 'wrong result'


if __name__ == '__main__':
    test_can_be_equal()
