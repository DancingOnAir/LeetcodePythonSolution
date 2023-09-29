class Solution:
    # match end with 25, 50, 00
    def minimumOperations(self, num: str) -> int:
        res = n = len(num)
        pattern_25 = []
        pattern_50 = []
        pattern_75 = []
        pattern_00 = []

        for i in range(n - 1, -1, -1):
            if num[i] == '0':
                if not pattern_50:
                    pattern_50.append(i)

                if not pattern_00:
                    pattern_00.append(i)
                else:
                    res = min(res, n - i - 2)
            elif num[i] == '5':
                if not pattern_25:
                    pattern_25.append(i)
                if not pattern_75:
                    pattern_75.append(i)
                if pattern_50:
                    res = min(res, n - i - 2)
            elif num[i] == '2':
                if pattern_25:
                    res = min(res, n - i - 2)
            elif num[i] == '7':
                if pattern_75:
                    res = min(res, n - i - 2)

        return n - 1 if (pattern_50 or pattern_00) and res == n else res


def test_minimum_operations():
    solution = Solution()
    assert solution.minimumOperations("2245047") == 2, 'wrong result'
    assert solution.minimumOperations("2908305") == 3, 'wrong result'
    assert solution.minimumOperations("10") == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_operations()
