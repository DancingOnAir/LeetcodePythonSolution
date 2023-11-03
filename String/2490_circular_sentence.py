class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0][0] != sentence[-1][-1]:
            return False

        words = sentence.split()
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
        return True


def test_is_circular_sentence():
    solution = Solution()
    assert solution.isCircularSentence("leetcode exercises sound delightful"), 'wrong result'
    assert solution.isCircularSentence("eetcode"), 'wrong result'
    assert not solution.isCircularSentence("Leetcode is cool"), 'wrong result'


if __name__ == '__main__':
    test_is_circular_sentence()
