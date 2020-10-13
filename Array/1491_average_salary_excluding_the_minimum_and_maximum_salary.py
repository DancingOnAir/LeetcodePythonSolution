from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / (len(salary) - 2)


def test_average():
    solution = Solution()

    salary1 = [4000, 3000, 1000, 2000]
    print(solution.average(salary1))

    salary2 = [1000, 2000, 3000]
    print(solution.average(salary2))

    salary3 = [6000, 5000, 4000, 3000, 2000, 1000]
    print(solution.average(salary3))

    salary4 = [8000, 9000, 2000, 3000, 6000, 1000]
    print(solution.average(salary4))


if __name__ == '__main__':
    test_average()
