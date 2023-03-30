from typing import List
from bisect import bisect_left


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        prime = [0]
        mx = max(nums)
        visit = [0] * (mx + 1)
        for i in range(2, mx + 1):
            if visit[i] == 0:
                prime.append(i)
                for j in range(i + i, mx + 1, i):
                    visit[j] = 1

        nums = [0] + nums
        for i in range(1, len(nums)):
            # if nums[i - 1] <= nums[i]:
            #     return False

            left, right = 0, len(prime) - 1
            while left <= right:
                mid = (left + right) // 2
                if prime[mid] + nums[i - 1] >= nums[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[i] > nums[i - 1] + prime[left - 1]:
                nums[i] -= prime[left - 1]
            else:
                return False

        return True


def test_prime_subOperation():
    solution = Solution()
    assert solution.primeSubOperation([4, 9, 6, 10]), 'wrong result'
    assert solution.primeSubOperation([6, 8, 11, 12]), 'wrong result'
    assert not solution.primeSubOperation([5, 8, 3]), 'wrong result'


if __name__ == '__main__':
    test_prime_subOperation()
