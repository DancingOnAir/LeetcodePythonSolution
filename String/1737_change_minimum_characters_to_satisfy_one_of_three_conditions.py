from collections import Counter


class Solution:
    # Operation 1 => make a below b:
    # We don't need to care how we make it, but there is definately a character, which separates the string a and string b
    # We can try this boundaray chararacter from b to z, and see how many steps to make string a below it, how many steps to make string b above or equal it. And just return the smallest steps among all boundary characters.
    # https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/discuss/1032042/Java-Detailed-Explanation-Find-the-Boundary-Letter
    def minCharacters(self, a: str, b: str) -> int:
        l1, l2 = len(a), len(b)

        c1 = Counter(ord(c) - 97 for c in a)
        c2 = Counter(ord(c) - 97 for c in b)

        # condition 3
        res = l1 + l2 - max((c1 + c2).values())
        for i in range(25):
            c1[i + 1] += c1[i]
            c2[i + 1] += c2[i]
            # condition 1
            res = min(res, l1 - c1[i] + c2[i])
            # condition 2
            res = min(res, l2 - c2[i] + c1[i])

        return res


def test_min_characters():
    solution = Solution()
    assert solution.minCharacters('aba', 'caa') == 2, 'wrong result'
    assert solution.minCharacters('dabadd', 'cda') == 3, 'wrong result'
    assert solution.minCharacters('acac', 'bd') == 1, 'wrong result'
    assert solution.minCharacters('ace', 'abe') == 2, 'wrong result'


if __name__ == '__main__':
    test_min_characters()
