class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        p = word.find(ch)
        return word[:p+1][::-1] + word[p+1:]


def test_reverse_prefix():
    solution = Solution()

    assert solution.reversePrefix("abcdefd", "d") == "dcbaefd", 'wrong result'
    assert solution.reversePrefix("xyxzxe", "z") == "zxyxxe", 'wrong result'
    assert solution.reversePrefix("abcd", "z") == "abcd", 'wrong result'


if __name__ == '__main__':
    test_reverse_prefix()
