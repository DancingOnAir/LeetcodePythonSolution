class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = []
        words = sentence.split()
        for i, w in enumerate(words):
            if w[0].lower() not in {'a', 'e', 'i', 'o', 'u'}:
                w = w[1:] + w[0]
            res.append(w + 'ma' + 'a' * (i + 1))
        return ' '.join(res)


def test_to_goat_latin():
    solution = Solution()
    assert solution.toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa", 'wrong result'
    assert solution.toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa", 'wrong result'


if __name__ == '__main__':
    test_to_goat_latin()
