from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)


def test_num_of_strings():
    solution = Solution()

    assert solution.numOfStrings(["a", "abc", "bc", "d"], "abc") == 3, 'wrong result'
    assert solution.numOfStrings(["a", "b", "c"], "aaaaabbbbb") == 2, 'wrong result'
    assert solution.numOfStrings(["a", "a", "a"], "ab") == 3, 'wrong result'


if __name__ == '__main__':
    test_num_of_strings()
