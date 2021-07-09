class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) & 1:
                return num[:i+1]
        return ''


def test_largest_odd_number():
    solution = Solution()

    assert solution.largestOddNumber("52") == "5", 'wrong result'
    assert solution.largestOddNumber("4206") == "", 'wrong result'
    assert solution.largestOddNumber("35427") == "35427", 'wrong result'


if __name__ == '__main__':
    test_largest_odd_number()
