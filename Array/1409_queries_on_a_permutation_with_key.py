from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []
        for i, val in enumerate(queries):
            pos = val - 1
            greater = []
            move_flag = False
            for num in queries[:i]:
                if not move_flag:
                    if num > val and num not in greater:
                        pos += 1
                        greater.append(num)
                    elif num == val:
                        pos = 0
                        move_flag = True
                        greater = []
                elif num == val:
                    pos = 0
                    greater = []
                else:
                    if num not in greater:
                        pos += 1
                        greater.append(num)

            res.append(pos)
        return res


def test_process_queries():
    solution = Solution()

    # queries1 = [3, 1, 2, 1]
    # m1 = 5
    # print(solution.processQueries(queries1, m1))
    #
    # queries2 = [4, 1, 2, 2]
    # m2 = 4
    # print(solution.processQueries(queries2, m2))
    #
    # queries3 = [7, 5, 5, 8, 3]
    # m3 = 8
    # print(solution.processQueries(queries3, m3))

    queries4 = [8, 7, 4, 2, 8, 1, 7, 7]
    m4 = 8
    print(solution.processQueries(queries4, m4))

    queries5 = [10, 7, 3, 3, 9, 4, 1, 4, 9, 9]
    m5 = 10
    print(solution.processQueries(queries5, m5))


if __name__ == '__main__':
    test_process_queries()
