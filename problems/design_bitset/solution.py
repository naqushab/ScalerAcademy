class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.b = [0]*size
        self.set = 0
        self.f = [1]*size

    def fix(self, idx: int) -> None:
        if self.b[idx] == 0:
            self.b[idx] = 1
            self.set += 1
            self.f[idx] = 0

    def unfix(self, idx: int) -> None:
        if self.b[idx] == 1:
            self.b[idx] = 0
            self.set -= 1
            self.f[idx] = 1

    def flip(self) -> None:
        self.b, self.f = self.f, self.b
        self.set = self.size - self.set

    def all(self) -> bool:
        return self.set == self.size

    def one(self) -> bool:
        return self.set > 0

    def count(self) -> int:
        return self.set

    def toString(self) -> str:
        return ''.join(map(str, self.b))

        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()