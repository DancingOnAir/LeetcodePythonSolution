class Solution:
    # z algorithm
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        z = [0] * n
        # z-box边界[left, right]
        left, right = 0, 0
        for i in range(1, n):
            if i <= right:
                z[i] = min(z[i - left], right - i + 1)
            while i + z[i] < n and word[z[i]] == word[i + z[i]]:
                left, right = i, i + z[i]
                z[i] += 1
            if i % k == 0 and z[i] >= n - i:
                return i // k
        return (n - 1) // k + 1


def test_minimum_time_to_initial_state():
    solution = Solution()
    assert solution.minimumTimeToInitialState("abacaba", 3) == 2, 'wrong result'
    assert solution.minimumTimeToInitialState("abacaba", 4) == 1, 'wrong result'
    assert solution.minimumTimeToInitialState("abcbabcd", 2) == 4, 'wrong result'


if __name__ == '__main__':
    test_minimum_time_to_initial_state()
