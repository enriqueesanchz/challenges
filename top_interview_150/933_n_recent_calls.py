class RecentCounter:

    def __init__(self):
        self.recent = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.recent.append(t)
        while self.recent[self.start] < t - 3000:
            self.start += 1

        return len(self.recent) - self.start
