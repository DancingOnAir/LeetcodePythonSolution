class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            temp = []
            for i in range(len(s) - 1):
                temp.append(str((int(s[i]) + int(s[i + 1])) % 10))
            s = ''.join(temp)
        return s[0] == s[1]


def test_has_same_digits():
    solution = Solution()
    assert solution.hasSameDigits("3902"), 'wrong result'
    assert not solution.hasSameDigits("34789"), 'wrong result'


if __name__ == '__main__':
    test_has_same_digits()
