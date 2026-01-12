from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for num in nums:
            if not num:
                count += 1
            elif count < k:
                return False
            else:
                count = 0
        return True

    def kLengthApart1(self, nums: List[int], k: int) -> bool:
        if not k:
            return True

        pre_index = -1
        for i, val in enumerate(nums):
            if val:
                if pre_index != -1 and i - pre_index - 1 < k:
                    return False
                pre_index = i
        return True


def test_k_length_apart():
    solution = Solution()

    nums1 = [1, 0, 0, 0, 1, 0, 0, 1]
    k1 = 2
    print(solution.kLengthApart(nums1, k1))

    nums2 = [1, 0, 0, 1, 0, 1]
    k2 = 2
    print(solution.kLengthApart(nums2, k2))

    nums3 = [1, 1, 1, 1, 1]
    k3 = 0
    print(solution.kLengthApart(nums3, k3))

    nums4 = [0, 1, 0, 1]
    k4 = 1
    print(solution.kLengthApart(nums4, k4))


if __name__ == '__main__':
    test_k_length_apart()
