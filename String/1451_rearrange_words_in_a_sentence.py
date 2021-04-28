class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()
        text[0] = text[0].lower()
        text.sort(key=lambda x: len(x))

        text[0] = text[0].capitalize()
        return ' '.join(text)


def test_arrange_words():
    solution = Solution()
    assert solution.arrangeWords('Leetcode is cool') == 'Is cool leetcode', 'wrong result'
    assert solution.arrangeWords('Keep calm and code on') == 'On and keep calm code', 'wrong result'
    assert solution.arrangeWords('To be or not to be') == 'To be or to be not', 'wrong result'


if __name__ == '__main__':
    test_arrange_words()
