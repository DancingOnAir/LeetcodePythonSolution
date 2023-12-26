class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last = 0
        for i, c in enumerate(number):
            if c == digit:
                last = i
                if i == len(number) - 1 or number[i + 1] > c:
                    return number[:i] + number[i+1:]
        return number[:last] + number[last+1:]


def test_remove_digit():
    solution = Solution()
    assert solution.removeDigit("123", "3") == "12", 'wrong result'
    assert solution.removeDigit("1231", "1") == "231", 'wrong result'
    assert solution.removeDigit("551", "5") == "51", 'wrong result'


if __name__ == '__main__':
    test_remove_digit()
