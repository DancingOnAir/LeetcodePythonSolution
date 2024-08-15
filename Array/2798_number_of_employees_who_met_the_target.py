from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(1 for x in hours if x >= target)


def test_number_of_employees_who_net_target():
    solution = Solution()
    assert solution.numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2) == 3, 'wrong result'
    assert solution.numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6) == 0, 'wrong result'


if __name__ == '__main__':
    test_number_of_employees_who_net_target()
