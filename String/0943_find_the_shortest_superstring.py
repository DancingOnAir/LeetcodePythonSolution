from typing import List


class Solution:
    # TODO
    def shortestSuperstring(self, words: List[str]) -> str:
        pass


def test_shortest_superstring():
    solution = Solution()

    assert solution.shortestSuperstring(["alex", "loves", "leetcode"]) == 'alexlovesleetcode'
    assert solution.shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]) == 'gctaagttcatgcatc'


if __name__ == '__main__':
    test_shortest_superstring()
