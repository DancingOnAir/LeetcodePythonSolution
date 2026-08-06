class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return []

        res = []
        pre = -1
        for x in sorted(nums):
            if pre == -1:
                pre = x
                continue
            pre += 1
            while pre != x:
                res.append(pre)
                pre += 1
        return res


def test_find_missing_elements():
    solution = Solution()
    assert solution.findMissingElements([1,4,2,5]) == [3], 'wrong result'
    assert solution.findMissingElements([7,8,6,9]) == [], 'wrong result'
    assert solution.findMissingElements([5,1]) == [2,3,4], 'wrong result'


if __name__ == '__main__':
    test_find_missing_elements()
