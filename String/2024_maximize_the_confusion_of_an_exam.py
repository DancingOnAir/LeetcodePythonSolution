from collections import Counter


class Solution:
    # improved sliding window
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = max_freq = 0
        c = Counter()
        for i in range(len(answerKey)):
            c[answerKey[i]] += 1
            max_freq = max(max_freq, c[answerKey[i]])

            if res - max_freq < k:
                res += 1
            else:
                c[answerKey[i - res]] -= 1
        return res

    # standard sliding window
    def maxConsecutiveAnswers1(self, answerKey: str, k: int) -> int:
        max_freq = i = 0
        c = Counter()
        for j, ans in enumerate(answerKey):
            c[ans] += 1
            max_freq = max(max_freq, c[ans])
            if j - i + 1 > max_freq + k:
                c[answerKey[i]] -= 1
                i += 1

        return len(answerKey) - i


def test_max_consecutive_answers():
    solution = Solution()

    assert solution.maxConsecutiveAnswers("TTFF", 2) == 4, 'wrong result'
    assert solution.maxConsecutiveAnswers("TFFT", 1) == 3, 'wrong result'
    assert solution.maxConsecutiveAnswers("TTFTTFTT", 1) == 5, 'wrong result'


if __name__ == '__main__':
    test_max_consecutive_answers()
