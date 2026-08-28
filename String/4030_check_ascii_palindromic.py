class Solution:
    def isPalindromic(self, s: str) -> bool:
        bin_str = ""
        for c in s:
            bin_str += f"{ord(c):08b}"

        for i in range(len(bin_str) // 2):
            if bin_str[i] != bin_str[len(bin_str) - i - 1]:
                return False
        return True

    def isPalindromic1(self, s: str) -> bool:
        bin_str = ""
        for c in s:
            bin_str += bin(ord(c))[2:].zfill(8)
        return bin_str == bin_str[::-1]


def test_is_palindromic():
    solution = Solution()
    assert solution.isPalindromic("ff"), 'wrong result'
    assert not solution.isPalindromic("leet"), 'wrong result'


if __name__ == '__main__':
    test_is_palindromic()
