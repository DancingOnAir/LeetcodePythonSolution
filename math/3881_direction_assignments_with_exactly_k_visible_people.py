from math import comb


class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        return comb(n - 1, k) * 2 % 1_000_000_007

def test_count_visible_people():
    solution = Solution()
    assert solution.countVisiblePeople(n=3, pos=0, k=2) == 2, 'wrong result'
    assert solution.countVisiblePeople(n=3, pos=1, k=0) == 2, 'wrong result'
    assert solution.countVisiblePeople(n=3, pos=2, k=1) == 4, 'wrong result'
    assert solution.countVisiblePeople(n=1, pos=0, k=0) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_visible_people()
