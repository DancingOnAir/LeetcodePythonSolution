class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ('1' in s) == ('1' in target)

    def makeStringsEqual1(self, s: str, target: str) -> bool:
        return (s == target) or (s.count('1') > 0 and target.count('1') > 0)


def test_make_string_equal():
    solution = Solution()
    assert solution.makeStringsEqual("1010", "0110"), 'wrong result'
    assert not solution.makeStringsEqual("11", "00"), 'wrong result'


if __name__ == '__main__':
    test_make_string_equal()
