from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if len(Counter(s[i: j])) == 3:
                    res += 1

        return res


def test_number_of_substrings():
    solution = Solution()
    assert solution.numberOfSubstrings('abcabc') == 10, 'wrong result'
    assert solution.numberOfSubstrings('aaacb') == 3, 'wrong result'
    assert solution.numberOfSubstrings('abc') == 1, 'wrong result'


if __name__ == '__main__':
    test_number_of_substrings()
