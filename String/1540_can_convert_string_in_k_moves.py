from collections import Counter


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        l1, l2 = len(s), len(t)
        if l1 != l2:
            return False

        counts = [0] * 26
        for i in range(l1):
            diff = (ord(t[i]) - ord(s[i]) + 26) % 26
            if not diff:
                continue

            if diff > k:
                return False

            counts[diff] += 1

        max_diff = 0
        for i, val in enumerate(counts):
            max_diff = max(max_diff, i + (val - 1) * 26)
            if max_diff > k:
                return False
        return True


def test_can_convert_string():
    solution = Solution()
    assert solution.canConvertString('input', 'ouput', 9), 'wrong result'
    assert not solution.canConvertString('abc', 'bcd', 10), 'wrong result'
    assert solution.canConvertString('aab', 'bbb', 27), 'wrong result'


if __name__ == '__main__':
    test_can_convert_string()
