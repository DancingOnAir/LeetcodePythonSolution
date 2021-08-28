from typing import List


class Solution:
    # https://leetcode.com/problems/find-unique-binary-string/discuss/1418687/Detailed-Explanation-O(N)-Java-C%2B%2B-Python-short-concise-code-Cantor's-Diagonalization
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join('1' if num[i] == '0' else '0' for i, num in enumerate(nums))

    # bin, string zfill
    def findDifferentBinaryString1(self, nums: List[str]) -> str:
        n = len(nums)
        s = set(nums)

        for i in range(2 ** n):
            cur = bin(i)[2:].zfill(n)
            if cur not in s:
                return cur


def test_find_different_binary_string():
    solution = Solution()

    assert solution.findDifferentBinaryString(["01", "10"]) == "11", 'wrong result'
    assert solution.findDifferentBinaryString(["00", "01"]) == "11", 'wrong result'
    assert solution.findDifferentBinaryString(["111", "011", "001"]) == "101", 'wrong result'


if __name__ == '__main__':
    test_find_different_binary_string()
