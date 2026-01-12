class Solution:
    def minOperations(self, s: str) -> int:
        return min(s[::2].count('1') + s[1::2].count('0'), s[::2].count('0') + s[1::2].count('1'))

    def minOperations2(self, s: str) -> int:
        diff = 0
        for i, c in enumerate(s):
            if int(c) != (i % 2):
                diff += 1
        return min(diff, len(s) - diff)

    def minOperations1(self, s: str) -> int:
        def helper(x):
            diff = 0
            for c in s:
                if x != c:
                    diff += 1
                x = '1' if x == '0' else '0'
            return diff
        return min(helper('1'), helper('0'))


def test_min_operations():
    solution = Solution()

    assert solution.minOperations('0100') == 1, 'wrong result'
    assert solution.minOperations('10') == 0, 'wrong result'
    assert solution.minOperations('1111') == 2, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
