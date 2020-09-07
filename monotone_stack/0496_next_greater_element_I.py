from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        stk = []
        element_in_nums2 = []
        next_greater_array = []
        res = []

        for i in range(len(nums2)):
            while stk and nums2[stk[-1]] < nums2[i]:
                element_in_nums2.append(nums2[stk.pop()])
                next_greater_array.append(nums2[i])
            stk.append(i)

        for num in nums1:
            if num in element_in_nums2:
                res.append(next_greater_array[element_in_nums2.index(num)])
            else:
                res.append(-1)

        return res

def test_next_greater_element():
    solution = Solution()

    nums11 = [4, 1, 2]
    nums12 = [1, 3, 4, 2]
    print(solution.nextGreaterElement(nums11, nums12))

    nums21 = [2, 4]
    nums22 = [1, 2, 3, 4]
    print(solution.nextGreaterElement(nums21, nums22))


if __name__ == '__main__':
    test_next_greater_element()
