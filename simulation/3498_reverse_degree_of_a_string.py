class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(i * (26 - ord(c) + ord('a')) for i, c in enumerate(s, 1))


def test_reverse_degree():
    solution = Solution()
    assert solution.reverseDegree('abc') == 148, 'wrong result'
    assert solution.reverseDegree('zaza') == 160, 'wrong result'


if __name__ == '__main__':
    test_reverse_degree()
