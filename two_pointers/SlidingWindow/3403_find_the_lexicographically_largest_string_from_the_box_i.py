class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        return max(word[i: i + len(word) - numFriends + 1] for i in range(len(word)))


def test_answer_string():
    solution = Solution()
    assert solution.answerString("dbca", 2) == "dbc", 'wrong result'
    assert solution.answerString("gggg", 4) == "g", 'wrong result'


if __name__ == '__main__':
    test_answer_string()
