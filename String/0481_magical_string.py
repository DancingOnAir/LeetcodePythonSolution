class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        cur = 2
        while len(s) < n:
            s += s[cur] * [(3 - s[-1])]
            cur += 1

        return s[:n].count(1)


def test_magical_string():
    solution = Solution()
    assert solution.magicalString(6) == 3, 'wrong result'
    assert solution.magicalString(1) == 1, 'wrong result'


if __name__ == '__main__':
    test_magical_string()
