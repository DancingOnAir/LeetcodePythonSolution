class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n * n, maxWeight // w)


def test_max_containers():
    solution = Solution()
    assert solution.maxContainers(2, 3, 15) == 4, 'wrong result'
    assert solution.maxContainers(3, 5, 20) == 4, 'wrong result'


if __name__ == '__main__':
    test_max_containers()
