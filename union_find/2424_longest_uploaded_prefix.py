class UF:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sz = [0] * n

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def unite(self, p, q):
        rp = self.find(p)
        rq = self.find(q)

        if rp != rq:
            self.parents[rp] = rq
            self.sz[rq] += self.sz[rp]

    def get_size(self, p):
        return self.sz[self.find(p)]


class LUPrefix:
    def __init__(self, n: int):
        self.uf = UF(n)
        self.n = n

    def upload(self, video: int) -> None:
        i = video - 1
        self.uf.sz[i] += 1
        if i > 0 and self.uf.get_size(i - 1) > 0:
            self.uf.unite(i - 1, i)
        if i + 1 < self.n and self.uf.get_size(i + 1) > 0:
            self.uf.unite(i, i + 1)

    def longest(self) -> int:
        return self.uf.get_size(0)


class LUPrefix1:
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
