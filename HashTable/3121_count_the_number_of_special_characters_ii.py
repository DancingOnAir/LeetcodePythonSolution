from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        if len(word) < 2:
            return 0

        flag = defaultdict(int)
        m = defaultdict(int)
        res = 0
        for c in word:
            cur = ord(c)
            if cur + 32 in m and flag[cur] == 0:
                flag[cur] = 1
                res += 1
            if cur - 32 in m:
                if flag[cur - 32] == 1:
                    res -= 1
                flag[cur - 32] = 2

            m[cur] = 1
        return res


def test_number_of_special_chars():
    solution = Solution()
    assert solution.numberOfSpecialChars("aaAbcBC") == 3, 'wrong result'
    assert solution.numberOfSpecialChars("abc") == 0, 'wrong result'
    assert solution.numberOfSpecialChars("AbBCab") == 0, 'wrong result'


if __name__ == '__main__':
    test_number_of_special_chars()
