from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i, r in enumerate(nums):
            for j, c in enumerate(r):
                if len(res) <= i + j:
                    res.append([])

                res[i + j].append(c)
        return [i for r in res for i in reversed(r)]

    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        count = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                count.append((i + j, j, i))

        count.sort()
        res = []
        for c in count:
            res.append(nums[c[2]][c[1]])
        return res

    # brute force, TLE
    def findDiagonalOrder1(self, nums: List[List[int]]) -> List[int]:
        row = len(nums)
        if row == 1:
            return nums[0]
        col = max([len(i) for i in nums])
        if col == 1:
            return list(*zip(*nums))

        res = []
        for i in range(row + col):
            r, c = i if i < row else row - 1, 0 if i < row else i - row + 1

            while r >= 0 and c < col:
                try:
                    res.append(nums[r][c])

                except IndexError:
                    continue
                finally:
                    r -= 1
                    c += 1
        return res


def test_find_diagonal_order():
    solution = Solution()

    nums1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.findDiagonalOrder(nums1))

    nums2 = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    print(solution.findDiagonalOrder(nums2))

    nums3 = [[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]]
    print(solution.findDiagonalOrder(nums3))

    nums4 = [[1, 2, 3, 4, 5, 6]]
    print(solution.findDiagonalOrder(nums4))


if __name__ == '__main__':
    test_find_diagonal_order()
