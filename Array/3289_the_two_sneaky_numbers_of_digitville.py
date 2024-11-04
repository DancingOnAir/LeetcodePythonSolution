from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        m = [0] * (len(nums) - 2)
        res = []
        for x in nums:
            m[x] += 1
            if m[x] == 2:
                res.append(x)
        return res


def test_get_sneaky_numbers():
    solution = Solution()
    assert sorted(solution.getSneakyNumbers([0, 1, 1, 0])) == [0, 1], 'wrong result'
    assert sorted(solution.getSneakyNumbers([0, 3, 2, 1, 3, 2])) == [2, 3], 'wrong result'
    assert solution.getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]) == [4, 5], 'wrong result'


if __name__ == '__main__':
    test_get_sneaky_numbers()
