class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return 2 * (min(x, y) * 2 + (x != y) + z)


def test_longest_string():
    solution = Solution()
    assert solution.longestString(2, 5, 1) == 12, 'wrong result'
    assert solution.longestString(3, 2, 2) == 14, 'wrong result'


if __name__ == '__main__':
    test_longest_string()
