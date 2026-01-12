class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        res = 0
        for a, b, c in zip(s1, s2, s3):
            if a == b == c:
                res += 1
            else:
                break
        return -1 if res == 0 else len(s1) + len(s2) + len(s3) - res * 3


def test_find_minimum_operations():
    solution = Solution()
    assert solution.findMinimumOperations("abc", "abb", "ab") == 2, 'wrong result'
    assert solution.findMinimumOperations("dac", "bac", "cac") == -1, 'wrong result'


if __name__ == '__main__':
    test_find_minimum_operations()
