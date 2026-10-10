class Solution:
    def minRotations(self, s: str) -> int:
        start = res = 0
        for c in s:
            target = int(c)
            res += min((target - start + 10) % 10, (start - target + 10) % 10)
            start = target
        return res


def test_min_rotations():
    solution = Solution()
    assert solution.minRotations("0192837465") == 25, 'wrong result'
    assert solution.minRotations("1200210200") == 12, 'wrong result'


if __name__ == "__main__":
    test_min_rotations()
