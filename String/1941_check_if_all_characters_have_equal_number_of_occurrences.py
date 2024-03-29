from collections import defaultdict, Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return all(i == len(s) // len(set(s)) for i in Counter(s).values())

    def areOccurrencesEqual2(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1

    def areOccurrencesEqual1(self, s: str) -> bool:
        memo = defaultdict(int)
        for c in s:
            memo[c] += 1

        return len(set(memo.values())) == 1


def test_are_occurrences_equal():
    solution = Solution()

    assert not solution.areOccurrencesEqual('tveixwaeoezcf'), 'wrong result'
    assert solution.areOccurrencesEqual('abacbc'), 'wrong result'
    assert not solution.areOccurrencesEqual('aaabb'), 'wrong result'


if __name__ == '__main__':
    test_are_occurrences_equal()
