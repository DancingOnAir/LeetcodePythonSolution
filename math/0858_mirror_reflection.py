from math import gcd


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        p = (p // g) % 2
        q = (q // g) % 2
        return 1 if p and q else 0 if p else 2


def test_mirror_refection():
    solution = Solution()
    assert solution.mirrorReflection(2, 1) == 2, 'wrong result'
    assert solution.mirrorReflection(3, 1) == 1, 'wrong result'


if __name__ == '__main__':
    test_mirror_refection()
