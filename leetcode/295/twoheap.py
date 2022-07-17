import heapq

class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []
        self.even = True
        

    def addNum(self, num: int) -> None:
        if self.even:
            heapq.heappush(self.smaller, -heapq.heappushpop(self.larger, num))
        else:
            heapq.heappush(self.larger, -heapq.heappushpop(self.smaller, -num))
            
        self.even = not self.even
            
        

    def findMedian(self) -> float:
        
        if not self.even:
            return -self.smaller[0]

        return (-self.smaller[0] + self.larger[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()