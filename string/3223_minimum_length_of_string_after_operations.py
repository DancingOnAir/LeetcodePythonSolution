from collections import defaultdict


class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
            if cnt[c] > 2:
                cnt[c] -= 2
        return sum(v for v in cnt.values())


def test_minimum_length():
    solution = Solution()
    assert solution.minimumLength("abaacbcbb") == 5, 'wrong result'
    assert solution.minimumLength("aa") == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_length()
