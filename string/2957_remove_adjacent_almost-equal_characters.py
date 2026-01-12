class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        res = []
        for i in range(1, len(word)):
            if abs(ord(word[i]) - ord(word[i - 1])) < 2 and (not res or res[-1] != i - 1):
                res.append(i)
        return len(res)

    def removeAlmostEqualCharacters1(self, word: str) -> int:
        res = left = 0
        for right in range(len(word)):
            if right > 0 and abs(ord(word[right - 1]) - ord(word[right])) > 1:
                res += (right - left) // 2
                left = right

        return res + (len(word) - left) // 2


def test_remove_almost_equal_characters():
    solution = Solution()
    assert solution.removeAlmostEqualCharacters("aa") == 1, 'wrong result'
    assert solution.removeAlmostEqualCharacters("aaaaa") == 2, 'wrong result'
    assert solution.removeAlmostEqualCharacters("abddez") == 2, 'wrong result'
    assert solution.removeAlmostEqualCharacters("zyxyxyz") == 3, 'wrong result'


if __name__ == '__main__':
    test_remove_almost_equal_characters()
