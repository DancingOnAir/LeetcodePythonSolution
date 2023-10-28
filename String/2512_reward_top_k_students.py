from typing import List
from heapq import heappush, heappop


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        hp = []

        for id, r in zip(student_id, report):
            point = 0
            for w in r.split():
                if w in positive_feedback:
                    point += 3
                if w in negative_feedback:
                    point -= 1
            if len(hp) < k:
                heappush(hp, [point, -id])
            else:
                popped = heappop(hp)
                if popped[0] > point:
                    heappush(hp, popped)
                elif popped[0] == point and -popped[1] < id:
                    heappush(hp, popped)
                else:
                    heappush(hp, [point, -id])

        res = []
        while hp:
            res.append(-heappop(hp)[1])
        res.reverse()
        return res

    # sort
    def topStudents1(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        m = []
        for i, r in enumerate(report):
            cur = 0
            for w in r.split():
                if w in positive_feedback:
                    cur += 3
                if w in negative_feedback:
                    cur -= 1
            m.append([student_id[i], cur])

        m.sort(key=lambda x: (-x[1], x[0]))
        return [a for a, b in m][:k]


def test_top_students():
    solution = Solution()
    assert solution.topStudents(["smart", "brilliant", "studious"], ["not"],
                                ["this student is studious", "the student is smart"], [1, 2], 2) == [1,
                                                                                                     2], 'wrong result'
    assert solution.topStudents(["smart", "brilliant", "studious"], ["not"],
                                ["this student is not studious", "the student is smart"], [1, 2], 2) == [2,
                                                                                                         1], 'wrong result'


if __name__ == '__main__':
    test_top_students()

