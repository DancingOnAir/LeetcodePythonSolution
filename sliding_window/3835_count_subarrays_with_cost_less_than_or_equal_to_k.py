from collections import deque


class Solution:
    # sliding window
    def countSubarrays(self, nums: list[int], k: int) -> int:
        left, res = 0, (len(nums) + 1) * len(nums) // 2
        min_q = deque()
        max_q = deque()

        for right, x in enumerate(nums):
            while max_q and max_q[-1] < x:
                max_q.pop()
            max_q.append(x)

            while min_q and min_q[-1] > x:
                min_q.pop()
            min_q.append(x)

            while (max_q[0] - min_q[0]) * (right - left + 1) > k:
                if nums[left] == max_q[0]:
                    max_q.popleft()
                if nums[left] == min_q[0]:
                    min_q.popleft()
                left += 1
            res -= left
        return res


def test_count_subarrays():
    solution = Solution()
    assert solution.countSubarrays([1, 3, 2], k=4) == 5, 'wrong result'
    assert solution.countSubarrays([5, 5, 5, 5], k=0) == 10, 'wrong result'
    assert solution.countSubarrays([1, 2, 3], k=0) == 3, 'wrong result'


if __name__ == '__main__':
    test_count_subarrays()
