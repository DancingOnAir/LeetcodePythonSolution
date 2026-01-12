from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[0::2]) == Counter(s2[0::2]) and Counter(s1[1::2]) == Counter(s2[1::2])

    def checkStrings1(self, s1: str, s2: str) -> bool:
        def helper(start):
            c1, c2 = Counter(), Counter()
            for i in range(start, len(s1), 2):
                c1[s1[i]] += 1
                c2[s2[i]] += 1
            return c1 == c2
        return helper(0) and helper(1)


def test_check_strings():
    solution = Solution()
    assert solution.checkStrings("abcdba", "cabdab"), 'wrong result'
    assert not solution.checkStrings("abe", "bea"), 'wrong result'


if __name__ == '__main__':
    test_check_strings()
