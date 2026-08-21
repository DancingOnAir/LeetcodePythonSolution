class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        return sum(abs(requests[i] - requests[i + 1]) for i in range(len(requests) - 1)) + requests[0]


def test_elevator_requests():
    assert Solution().elevatorRequests(5, requests=[2, 1, 4, 3]) == 7, 'wrong result'
    assert Solution().elevatorRequests(3, requests=[2, 0, 0]) == 4, 'wrong result'


if __name__ == '__main__':
    test_elevator_requests()
