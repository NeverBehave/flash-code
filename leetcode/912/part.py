class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.recurSort(0, len(nums) - 1)
        
        return self.nums
    
    def recurSort(self, left, right):
        if left < right:
            pidx = self.partition(left, right)
            self.recurSort(left, pidx - 1)
            self.recurSort(pidx + 1, right)
    
    def partition(self, left, right):
        pivot = left
        index = pivot + 1
        i = index
        while i <= right:
            if self.nums[pivot] > self.nums[i]:
                self.swap(i, index)
                index += 1
            i += 1
        
        final = index - 1
        self.swap(final, pivot)
        
        return final
    
    def swap(self, a, b):
        self.nums[a], self.nums[b] = self.nums[b], self.nums[a]