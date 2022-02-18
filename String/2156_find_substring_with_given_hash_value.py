class Solution:
    # sliding window + rolling hash
    # traverse from end instead of front, coz hash *= p works easier than hash /= p
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        cur_hash = 0
        res = left = right = len(s) - 1

        while left >= 0:
            cur_hash = (cur_hash * power + (ord(s[left]) - 96)) % modulo

            if right - left + 1 == k:
                if cur_hash % modulo == hashValue:
                    res = left

                cur_hash = (cur_hash - (ord(s[right]) - 96) * pow(power, k-1, modulo)) % modulo
                right -= 1
            left -= 1
        return s[res: res + k]


def test_sub_str_hash():
    solution = Solution()
    assert solution.subStrHash('leetcode', 7, 20, 2, 0) == 'ee', 'wrong result'
    assert solution.subStrHash('fbxzaad', 31, 100, 3, 32) == 'fbx', 'wrong result'
    assert solution.subStrHash("cbmzzngpnfyzoexfnzxhhyvzxibaijgfvaleowaqjllkgoercyiptkugzgcxobn", 83, 56, 27, 23) == "hyvzxibaijgfvaleowaqjllkgoe", 'wrong result'


if __name__ == '__main__':
    test_sub_str_hash()
