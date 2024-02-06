class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        res = 1
        for i in range(1, int(n / k) + 1):
            if word[:n-k*i] == word[k*i:]:
                return res
            res += 1
        return res


def test_minimum_time_to_initial_state():
    solution = Solution()
    assert solution.minimumTimeToInitialState("abacaba", 3) == 2, 'wrong result'
    assert solution.minimumTimeToInitialState("abacaba", 4) == 1, 'wrong result'
    assert solution.minimumTimeToInitialState("abcbabcd", 2) == 4, 'wrong result'


if __name__ == '__main__':
    test_minimum_time_to_initial_state()
