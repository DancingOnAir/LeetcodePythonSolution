class LUPrefix:
    def __init__(self, n: int):
        self.n = n
        self.parent = [0] * (n + 1)

    def upload(self, video: int) -> None:
        self.parent[video] = video
        if video == 1 or self.parent[video - 1] != 0:
            self.parent[video - 1] = video
        if video < self.n and self.parent[video + 1] != 0:
            self.parent[video] = self.parent[video + 1]

    def longest(self) -> int:
        return self.find(0)

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p


def test_lu_prefix():
    obj = LUPrefix(4)
    obj.upload(3)
    assert obj.longest() == 0, 'wrong result'
    obj.upload(1)
    assert obj.longest() == 1, 'wrong result'
    obj.upload(2)
    assert obj.longest() == 3, 'wrong result'


if __name__ == '__main__':
    test_lu_prefix()
