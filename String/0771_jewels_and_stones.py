class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        return sum(s in jewels for s in stones)


def test_num_jewels_in_stones():
    solution = Solution()
    assert solution.numJewelsInStones("aA", "aAAbbbb") == 3, 'wrong result'
    assert solution.numJewelsInStones("z", "ZZ") == 0, 'wrong result'


if __name__ == '__main__':
    test_num_jewels_in_stones()
