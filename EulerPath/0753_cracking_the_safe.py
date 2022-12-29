from collections import defaultdict


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        pass


def test_crack_safe():
    solution = Solution()
    assert solution.crackSafe(1, 2) == "10", 'wrong result'
    assert solution.crackSafe(2, 2) == "01100", 'wrong result'


if __name__ == '__main__':
    test_crack_safe()
