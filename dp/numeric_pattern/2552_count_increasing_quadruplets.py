class Solution:
    # 1324
    def countQuadruplets(self, nums: list[int]) -> int:
        cnt4 = 0
        cnt3 = [0] * len(nums)
        for l in range(2, len(nums)):
            cnt2 = 0
            for j in range(l):
                # 3 < 4
                if nums[j] < nums[l]:
                    cnt4 += cnt3[j]
                    # 把j当作i，把l当作k，现在nums[i] < nums[k], 1 < 2
                    cnt2 += 1
                else:
                    # 把l当作k，现在nums[j] > nums[k], 3 > 2
                    cnt3[j] += cnt2
        return cnt4


def test_count_quadruplets():
    solution = Solution()
    assert solution.countQuadruplets([1,3,2,4,5]) == 2, 'wrong result'
    assert solution.countQuadruplets([1,2,3,4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_quadruplets()

