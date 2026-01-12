class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        if s.count(' ') < k:
            return s

        i, pos = 0, -1
        while i < k:
            pos = s.find(' ', pos + 1)
            i += 1
        return s[: pos]

    def truncateSentence1(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


def test_truncate_sentence():
    solution = Solution()
    # assert solution.truncateSentence('Hello how are you Contestant', 4) == 'Hello how are you', 'wrong result'
    # assert solution.truncateSentence('What is the solution to this problem', 4) == 'What is the solution'
    assert solution.truncateSentence('chopper is not a tanuki', 5) == 'chopper is not a tanuki', 'wrong result'


if __name__ == '__main__':
    test_truncate_sentence()
