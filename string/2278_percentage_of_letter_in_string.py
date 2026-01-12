class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(s.count(letter) / len(s) * 100)


def test_percentage_letter():
    solution = Solution()
    assert solution.percentageLetter("foobar",  "o") == 33, 'wrong result'
    assert solution.percentageLetter("jjjj", "k") == 0, 'wrong result'


if __name__ == '__main__':
    test_percentage_letter()
