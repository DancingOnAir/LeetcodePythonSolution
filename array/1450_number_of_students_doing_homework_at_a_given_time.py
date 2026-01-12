from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(i <= queryTime <= j for i, j in zip(startTime, endTime))

    def busyStudent1(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1
        return res


def test_busy_student():
    solution = Solution()

    startTime1 = [1, 2, 3]
    endTime1 = [3, 2, 7]
    queryTime1 = 4
    print(solution.busyStudent(startTime1, endTime1, queryTime1))

    startTime2 = [4]
    endTime2 = [4]
    queryTime2 = 4
    print(solution.busyStudent(startTime2, endTime2, queryTime2))

    startTime3 = [4]
    endTime3 = [4]
    queryTime3 = 5
    print(solution.busyStudent(startTime3, endTime3, queryTime3))


if __name__ == '__main__':
    test_busy_student()
