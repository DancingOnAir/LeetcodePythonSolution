class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for i in range(2, n + 1):
            res = (res + k) % i
        return res + 1


def test_find_the_winner():
    solution = Solution()
    assert solution.findTheWinner(5, 2) == 3, 'wrong result'
    assert solution.findTheWinner(6, 5) == 1, 'wrong result'


if __name__ == '__main__':
    test_find_the_winner()
