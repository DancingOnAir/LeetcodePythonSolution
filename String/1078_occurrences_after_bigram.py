from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = list()
        words = text.split()
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                res.append(words[i + 2])
        return res


def test_find_occurrences():
    solution = Solution()

    assert solution.findOcurrences("alice is a good girl she is a good student", "a", "good") == ["girl", "student"], 'wrong result'
    assert solution.findOcurrences("we will we will rock you", "we", "will") == ["we", "rock"], 'wrong result'


if __name__ == '__main__':
    test_find_occurrences()
