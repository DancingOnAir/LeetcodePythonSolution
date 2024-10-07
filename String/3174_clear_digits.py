class Solution:
    def clearDigits(self, s: str) -> str:

        pass


def test_clear_digits():
    solution = Solution()
    assert solution.clearDigits("abc") == "abc", 'wrong result'
    assert solution.clearDigits("cb34") == "", 'wrong result'


if __name__ == '__main__':
    test_clear_digits()
