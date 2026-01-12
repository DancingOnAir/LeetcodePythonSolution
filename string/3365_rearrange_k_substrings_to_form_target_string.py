from collections import Counter


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        k = n // k
        cnt1, cnt2 = Counter(), Counter()
        for i in range(0, n, k):
            cnt1[s[i: i+k]] += 1
            cnt2[t[i: i+k]] += 1
        return cnt1 == cnt2


def test_is_possible_to_rearrange():
    solution = Solution()
    assert solution.isPossibleToRearrange("abcd", "cdab", 2), 'wrong result'
    assert solution.isPossibleToRearrange("aabbcc", "bbaacc", 3), 'wrong result'
    assert not solution.isPossibleToRearrange("aabbcc", "bbaacc", 2), 'wrong result'


if __name__ == '__main__':
    test_is_possible_to_rearrange()
