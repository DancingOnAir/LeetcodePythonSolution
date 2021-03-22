class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        l1, l2 = len(s), len(t)
        res = 0

        for i in range(l1):
            for j in range(l2):
                diff = 0
                k = 0
                while i + k < l1 and j + k < l2:
                    if s[i + k] != t[j + k]:
                        diff += 1

                    if diff == 1:
                        res += 1
                    elif diff == 2:
                        break
                    k += 1

        return res


def test_count_substrings():
    solution = Solution()
    assert solution.countSubstrings('aba', 'baba') == 6, 'wrong result'
    assert solution.countSubstrings('ab', 'bb') == 3, 'wrong result'
    assert solution.countSubstrings('a', 'a') == 0, 'wrong result'
    assert solution.countSubstrings('abe', 'bbc') == 10, 'wrong result'


if __name__ == '__main__':
    test_count_substrings()
