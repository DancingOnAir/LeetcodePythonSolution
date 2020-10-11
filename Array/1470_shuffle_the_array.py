from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [num for tup in zip(nums[:n], nums[n:]) for num in tup]

    def shuffle1(self, nums: List[int], n: int) -> List[int]:
        res = [0] * 2 * n
        for i, val in enumerate(nums):
            if i < n:
                res[i * 2] = val
            else:
                res[2 * (i - n) + 1] = val
        return res


def test_shuffle():
    """
    tests shuffle function, contains 3 testing cases
    :return:
    """
    solution = Solution()

    nums1 = [2, 5, 1, 3, 4, 7]
    n1 = 3
    print(solution.shuffle(nums1, n1))

    nums2 = [1, 2, 3, 4, 4, 3, 2, 1]
    n2 = 4
    print(solution.shuffle(nums2, n2))

    nums3 = [1, 1, 2, 2]
    n3 = 2
    print(solution.shuffle(nums3, n3))


if __name__ == '__main__':
    test_shuffle()

