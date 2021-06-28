class Solution:
    # stack
    # states([p, q]), here p represents the min operations of current num changes to 0
    # q represents the min operations of current num changes to 1
    def minOperationsToFlip(self, expression: str) -> int:
        # sample for operation sequence
        # print(eval("1|1&0"))
        states = list()
        ops = list()

        for i, c in enumerate(expression):
            if c in '01)':
                if c == '0':
                    states.append([0, 1])
                elif c == '1':
                    states.append([1, 0])
                else:
                    if ops[-1] == '(':
                        ops.pop()

                if ops and ops[-1] != '(':
                    op = ops.pop()
                    p2, q2 = states.pop()
                    p1, q1 = states.pop()
                    if op == '&':
                        states.append([min(p1, p2), min(q1 + q2, min(q1, q2) + 1)])
                    else:
                        states.append([min(p1 + p2, min(q1, q2) + 1), min(q1, q2)])
            else:
                ops.append(c)
        return max(states[-1])


def test_min_operations_to_flip():
    solution = Solution()

    assert solution.minOperationsToFlip("1&(0|1)") == 1, 'wrong result'
    assert solution.minOperationsToFlip("(0&0)&(0&0&0)") == 3, 'wrong result'
    assert solution.minOperationsToFlip("(0|(1|0&1))") == 1, 'wrong result'


if __name__ == '__main__':
    test_min_operations_to_flip()
