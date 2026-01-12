from itertools import pairwise


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a) - ord(b)) for a, b in pairwise(s))


def test_score_of_string():
    solution = Solution()
    assert solution.scoreOfString("hello") == 13, 'wrong result'
    assert solution.scoreOfString("zaz") == 50, 'wrong result'


if __name__ == '__main__':
    test_score_of_string()
