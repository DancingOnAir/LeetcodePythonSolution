class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        pass


def test_sub_str_hash():
    solution = Solution()
    assert solution.subStrHash('leetcode', 7, 20, 2, 0) == 'ee', 'wrong result'
    assert solution.subStrHash('fbxzaad', 31, 100, 3, 32) == 'fbx', 'wrong result'


if __name__ == '__main__':
    test_sub_str_hash()
