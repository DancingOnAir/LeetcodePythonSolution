class Solution:
    # consider s1 is the shorter sentence, then we can try to insert a sentence to make it equal with s2
    # there are 3 situations:
    # 1. s1 + new s == s2 -> s1 == s2[:l1]
    # 2. new s + s1 == s2 -> s1 == s2[-l1:]
    # 3. if s1 = a + b and a + new s + b = s2 -> s1[:i] == s2[:i] and s1[i:] == s2[-(l1-i):] for i in range(1, l1)
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = sentence1.split(), sentence2.split()
        l1, l2 = len(s1), len(s2)
        if l1 == l2:
            return s1 == s2
        elif l1 > l2:
            return self.areSentencesSimilar(sentence2, sentence1)

        if s1 == s2[:l1]:
            return True
        if s1 == s2[-l1:]:
            return True
        for i in range(1, l1):
            if s1[: i] == s2[: i] and s1[i:] == s2[-(l1 - i):]:
                return True
        return False


def test_are_sentences_similar():
    solution = Solution()
    assert solution.areSentencesSimilar('My name is Haley', 'My Haley'), 'wrong result'
    assert not solution.areSentencesSimilar('of', 'A lot of words'), 'wrong result'
    assert solution.areSentencesSimilar('Eating right now', 'Eating'), 'wrong result'
    assert not solution.areSentencesSimilar('Luky', 'Lucccky'), 'wrong result'


if __name__ == '__main__':
    test_are_sentences_similar()
