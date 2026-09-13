class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        nums = set()
        n = len(digits)
        for i in range(n):
            if digits[i] != 0:
                for j in range(n):
                    if i != j:
                        for k in range(n):
                            if k != i and k != j and digits[k] % 2 == 0:
                                nums.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return len(nums)


def test_total_numbers():
    solution = Solution()
    assert solution.totalNumbers([1,2,3,4]) == 12, 'wrong result'
    assert solution.totalNumbers([0,2,2]) == 2, 'wrong result'
    assert solution.totalNumbers([6,6,6]) == 1, 'wrong result'
    assert solution.totalNumbers([1,3,5]) == 0, 'wrong result'


if __name__ == '__main__':
    test_total_numbers()

