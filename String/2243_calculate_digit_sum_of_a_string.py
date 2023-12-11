class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            cur = map(lambda x: str(sum(int(c) for c in x)), [s[i: i+k] for i in range(0, len(s), k)])
            s = ''.join(cur)
        return s


def test_digit_sum():
    solution = Solution()
    assert solution.digitSum("11111222223", 3) == "135", 'wrong result'
    assert solution.digitSum("00000000", 3) == "000", 'wrong result'


if __name__ == '__main__':
    test_digit_sum()
