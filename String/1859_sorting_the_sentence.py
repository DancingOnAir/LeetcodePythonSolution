class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join([x[:-1] for x in sorted(s.split(), key=lambda x: x[-1])])


def test_sort_sentence():
    solution = Solution()
    assert solution.sortSentence('is2 sentence4 This1 a3') == "This is a sentence", 'wrong result'
    assert solution.sortSentence('Myself2 Me1 I4 and3') == "Me Myself and I", 'wrong result'


if __name__ == '__main__':
    test_sort_sentence()
