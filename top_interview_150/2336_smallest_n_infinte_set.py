class SmallestInfiniteSet:

    def __init__(self):
        self.cur = 1
        self.set = set()

    def popSmallest(self) -> int:
        if self.set:
            n = min(self.set)
            self.set.remove(n)
        else:
            n = self.cur
            self.cur += 1
        return n

    def addBack(self, num: int) -> None:
        if num < self.cur:
            self.set.add(num)
