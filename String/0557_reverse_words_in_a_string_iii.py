class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(ss[::-1] for ss in s.split())


def test_reverse_words():
    solution = Solution()
    assert solution.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc", 'wrong result'
    assert solution.reverseWords("Mr Ding") == "rM gniD", 'wrong result'


if __name__ == '__main__':
    test_reverse_words()
