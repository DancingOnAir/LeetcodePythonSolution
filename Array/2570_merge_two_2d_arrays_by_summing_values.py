from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = list()
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                res.append(nums2[j])
                j += 1
            elif j >= len(nums2):
                res.append(nums1[i])
                i += 1
            else:
                if nums1[i][0] == nums2[j][0]:
                    res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                    i += 1
                    j += 1
                elif nums1[i][0] < nums2[j][0]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1

        return res


def test_merge_arrays():
    solution = Solution()
    assert solution.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]) == [[1, 6], [2, 3], [3, 2],
                                                                                        [4, 6]], 'wrong result'
    assert solution.mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]) == [[1, 3], [2, 4], [3, 6], [4, 3],
                                                                                [5, 5]], 'wrong result'


if __name__ == '__main__':
    test_merge_arrays()
