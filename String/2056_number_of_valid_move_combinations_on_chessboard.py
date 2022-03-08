class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        pass


def test_count_combinations():
    solution = Solution()
    assert solution.countCombinations(["rook"], [[1,1]]) == 15, 'wrong result'
    assert solution.countCombinations(["queen"], [[1,1]]) == 22, 'wrong result'
    assert solution.countCombinations(["bishop"], [[4,3]]) == 12, 'wrong result'


if __name__ == '__main__':
    test_count_combinations()
