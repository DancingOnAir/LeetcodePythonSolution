class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, w in enumerate(sentence.split()):
            if searchWord == w[:len(searchWord)]:
                return i + 1
        return -1

    def isPrefixOfWord1(self, sentence: str, searchWord: str) -> int:
        for i, w in enumerate(sentence.split()):
            if w.startswith(searchWord):
                return i + 1
        return -1


def test_is_prefix_of_word():
    solution = Solution()
    assert solution.isPrefixOfWord("i love eating burger", "burg") == 4, 'wrong result'
    assert solution.isPrefixOfWord("this problem is an easy problem", "pro") == 2, 'wrong result'
    assert solution.isPrefixOfWord("i am tired", "you") == -1, 'wrong result'
    assert solution.isPrefixOfWord("i use triple pillow", "pill") == 4, 'wrong result'
    assert solution.isPrefixOfWord("hello from the other side", "they") == -1, 'wrong result'


if __name__ == '__main__':
    test_is_prefix_of_word()
