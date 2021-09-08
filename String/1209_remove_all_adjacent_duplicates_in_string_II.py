from itertools import groupby


class Solution:
    # itertools.groupby solution TLE
    def removeDuplicates(self, s: str, k: int) -> str:
        while True:
            new_s = ''
            for c, g in groupby(s):
                n = len(list(g))
                if n > k:
                    new_s += c * (n - k)
                elif n < k:
                    new_s += c * n

            if new_s == s:
                break
            s = new_s

        return new_s


def test_remove_duplicates():
    solution = Solution()

    assert solution.removeDuplicates("abcd", 2) == "abcd", 'wrong result'
    assert solution.removeDuplicates("deeedbbcccbdaa", 3) == "aa", 'wrong result'
    assert solution.removeDuplicates("pbbcggttciiippooaais", 2) == "ps", 'wrong result'


if __name__ == '__main__':
    test_remove_duplicates()
