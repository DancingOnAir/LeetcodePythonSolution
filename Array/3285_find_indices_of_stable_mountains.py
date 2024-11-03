from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]


def test_stable_mountains():
    solution = Solution()
    assert solution.stableMountains([1,2,3,4,5], 2) == [3, 4], 'wrong result'
    assert solution.stableMountains([10,1,10,1,10], 3) == [1,3], 'wrong result'
    assert solution.stableMountains([10,1,10,1,10], 10) == [], 'wrong result'


if __name__ == '__main__':
    test_stable_mountains()
