class Solution:
    def reinitializePermutation(self, n: int) -> int:
        i = step = 1
        while True:
            i = (n - 1 + i) // 2 if i & 1 else i // 2
            if i == 1:
                return step
            step += 1


def test_reinitialize_permutation():
    solution = Solution()
    assert solution.reinitializePermutation(2) == 1, 'wrong result'
    assert solution.reinitializePermutation(4) == 2, 'wrong result'
    assert solution.reinitializePermutation(6) == 4, 'wrong result'


if __name__ == '__main__':
    test_reinitialize_permutation()
