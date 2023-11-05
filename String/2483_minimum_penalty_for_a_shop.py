class Solution:
    def bestClosingTime(self, customers: str) -> int:
        mi = penalty = customers.count('Y')
        res = 0
        for i, c in enumerate(customers, 1):
            if c == 'N':
                penalty += 1
            else:
                penalty -= 1
                if penalty < mi:
                    mi = penalty
                    res = i
        return res

    def bestClosingTime1(self, customers: str) -> int:
        n = len(customers)
        Y, N = [0], [0]
        for i in range(len(customers) - 1, -1, -1):
            if customers[i] == 'Y':
                Y.append(Y[-1] + 1)
            else:
                Y.append(Y[-1])
        Y.reverse()

        for i in range(n):
            if customers[i] == 'N':
                N.append(N[-1] + 1)
            else:
                N.append(N[-1])

        res, penalty = -1, float('inf')
        for i in range(n + 1):
            if Y[i] + N[i] < penalty:
                penalty = Y[i] + N[i]
                res = i
        return res


def test_best_closing_time():
    solution = Solution()
    assert solution.bestClosingTime("YYNY") == 2, 'wrong result'
    assert solution.bestClosingTime("NNNNN") == 0, 'wrong result'
    assert solution.bestClosingTime("YYYY") == 4, 'wrong result'


if __name__ == '__main__':
    test_best_closing_time()
