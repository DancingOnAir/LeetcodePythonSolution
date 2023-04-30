class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = '01'
        for i in range(25):
            if res in s:
                res = '0' + res + '1'
            else:
                break
        return len(res) - 2

    def findTheLongestBalancedSubstring1(self, s: str) -> int:
        i = 0
        res = 0
        while i < len(s) and s[i] == '1':
            i += 1

        while i < len(s):
            j = i
            while i < len(s) and s[i] == '0':
                i += 1

            zeros = i - j
            j = i
            while i < len(s) and s[i] == '1':
                i += 1
            ones = i - j

            res = max(res, min(zeros, ones) * 2)
        return res


def test_find_the_longest_balanced_substring():
    solution = Solution()
    assert solution.findTheLongestBalancedSubstring("01000111") == 6, 'wrong result'
    assert solution.findTheLongestBalancedSubstring("00111") == 4, 'wrong result'
    assert solution.findTheLongestBalancedSubstring("111") == 0, 'wrong result'


if __name__ == '__main__':
    test_find_the_longest_balanced_substring()
