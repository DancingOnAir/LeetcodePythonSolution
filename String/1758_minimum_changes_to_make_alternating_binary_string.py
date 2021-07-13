class Solution:
    def minOperations(self, s: str) -> int:
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
