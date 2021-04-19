class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = [0] * 26
        for c in sentence:
            counter[ord(c) - 97] += 1

        return counter.count(0) == 0


def test_check_if_pangram():
    solution = Solution()
    assert solution.checkIfPangram('thequickbrownfoxjumpsoverthelazydog'), 'wrong result'
    assert not solution.checkIfPangram('leetcode'), 'wrong result'


if __name__ == '__main__':
    test_check_if_pangram()
