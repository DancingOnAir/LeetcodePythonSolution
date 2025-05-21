class Solution:
    # https://leetcode.cn/problems/airplane-seat-assignment-probability/solutions/2858975/tu-jie-mei-xiang-ming-bai-yi-zhang-tu-mi-8bn4/
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5


def test_nth_person_gets_nth_seat():
    solution = Solution()
    assert solution.nthPersonGetsNthSeat(1) == 1.0, 'wrong result'
    assert solution.nthPersonGetsNthSeat(2) == 0.5, 'wrong result'


if __name__ == '__main__':
    test_nth_person_gets_nth_seat()



