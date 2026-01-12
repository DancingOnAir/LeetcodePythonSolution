from collections import Counter


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        return len(word) // k - max(Counter(word[i: i+k] for i in range(0, len(word), k)).values())

    def minimumOperationsToMakeKPeriodic1(self, word: str, k: int) -> int:
        cnt = Counter()
        for i in range(0, len(word), k):
            cnt[word[i: i+k]] += 1

        return len(word) // k - max(cnt.values())


def test_minimum_operations_to_make_k_periodic():
    solution = Solution()
    assert solution.minimumOperationsToMakeKPeriodic("leetcodeleet", 4) == 1, "wrong result"
    assert solution.minimumOperationsToMakeKPeriodic("leetcoleet", 2) == 3, "wrong result"


if __name__ == '__main__':
    test_minimum_operations_to_make_k_periodic()
