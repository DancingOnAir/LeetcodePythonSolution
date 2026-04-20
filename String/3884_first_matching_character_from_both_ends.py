class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        for i in range(len(s) // 2 + 1):
            if s[i] == s[~i]:
                return i
        return -1


def test_first_matching_index():
    solution = Solution()
    assert solution.firstMatchingIndex("abcacbd") == 1, 'wrong result'
    assert solution.firstMatchingIndex("abc") == 1, 'wrong result'
    assert solution.firstMatchingIndex("abcdab") == -1, 'wrong result'


if __name__ == '__main__':
    test_first_matching_index()
