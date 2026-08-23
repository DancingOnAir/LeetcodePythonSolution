class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        res = float('inf')
        for i in range(n):
            op = i
            for j in range(n // 2):
                diff = abs(ord(s[(i + j) % n]) - ord(s[(i - 1 - j) % n]))
                op += min(diff, 26 - diff)
                if op > res:
                    break
            res = min(res, op)
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations('abc') == 2, 'wrong result'
    assert solution.minOperations('yb') == 3, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
