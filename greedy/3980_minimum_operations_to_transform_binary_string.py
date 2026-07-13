class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        n = len(s1)
        if n == 1 and s1[0] == '1' and s2[0] == '0':
            return -1

        s = list(s1)
        res = 0
        for i in range(n):
            if s[i] == s2[i]:
                continue
            if s[i] == '0':
                res += 1
            elif i < n - 1 and s[i + 1] == '1':
                res += 1
                s[i + 1] = '0'
            else:
                res += 2
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations("11", s2 = "00") == 1, 'wrong result'
    assert solution.minOperations("01", s2 = "10") == 3, 'wrong result'
    assert solution.minOperations("1", s2 = "0") == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
