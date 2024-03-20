from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(int(max(x) * len(x)) for x in map(str, nums))


def test_sum_of_encrypted_int():
    solution = Solution()
    assert solution.sumOfEncryptedInt([1, 2, 3]) == 6, 'wrong result'
    assert solution.sumOfEncryptedInt([10, 21, 31]) == 66, 'wrong result'


if __name__ == '__main__':
    test_sum_of_encrypted_int()
