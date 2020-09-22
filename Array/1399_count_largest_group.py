from typing import List


class Solution:
    def countLargestGroup(self, n: int) -> int:
        def calculateDigits(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        res = [0] * 37
        for i in range(1, n + 1):
            res[calculateDigits(i)] += 1

        return res.count(max(res))


def test_count_largest_group():
    solution = Solution()

    print(solution.countLargestGroup(13))
    print(solution.countLargestGroup(2))
    print(solution.countLargestGroup(15))
    print(solution.countLargestGroup(24))


if __name__ == '__main__':
    test_count_largest_group()
