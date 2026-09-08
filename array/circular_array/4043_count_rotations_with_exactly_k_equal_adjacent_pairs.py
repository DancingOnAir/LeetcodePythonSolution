class Solution:
    def countRotations(self, s: str, k: int) -> int:
        tot = 0
        n = len(s)
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                tot += 1
        if s[0] == s[-1]:
            tot += 1

        if k == tot:
            return n - tot

        if k == tot - 1:
            return tot
        return 0


def test_count_rotations():
    solution = Solution()
    assert solution.countRotations("aab", 1) == 2, 'wrong result'
    assert solution.countRotations("abca", 0) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_rotations()
