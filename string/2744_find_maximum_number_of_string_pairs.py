from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        m = set()
        res = 0
        for word in words:
            if word in m:
                res += 1
            else:
                m.add(word[::-1])
        return res


def test_maximum_number_of_string_pairs():
    solution = Solution()
    assert solution.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]) == 2, 'wrong result'
    assert solution.maximumNumberOfStringPairs(["ab","ba","cc"]) == 1, 'wrong result'
    assert solution.maximumNumberOfStringPairs(["aa","ab"]) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_number_of_string_pairs()
