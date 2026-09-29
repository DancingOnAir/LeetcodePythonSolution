class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        return sum(source) == sum(target)


def test_can_transform():
    solution = Solution()
    assert solution.canTransform([1, 2, 3], [0, 2, 4]), 'wrong result'
    assert solution.canTransform([-5, -5], target=[-15, 5]), 'wrong result'
    assert not solution.canTransform([1, 2, 1], target=[0, 2, 5]), 'wrong result'


if __name__ == '__main__':
    test_can_transform()
