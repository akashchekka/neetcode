class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        from heapq import heappush, heappop
        small = self.small
        large = self.large

        heappush(small, -1 * num)

        if small and large and (-1 * small[0]) > large[0]:
                val = -1 * heappop(small)
                heappush(large, val)

        if len(small) > len(large) + 1:
            val = -1 * heappop(small)
            heappush(large, val)

        if len(large) > len(small) + 1:
            val = heappop(large)
            heappush(small, -1 * val)

    def findMedian(self) -> float:
        small = self.small
        large = self.large

        if len(small) > len(large):
            return -1 * small[0]

        if len(large) > len(small):
            return large[0]

        return (-1 * small[0] + large[0]) / 2
        