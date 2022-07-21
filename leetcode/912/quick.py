class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.recurSort(nums ,0, len(nums) - 1)
        
        return nums
    
    def recurSort(self, nums, left, right):
        if (left >= right):
            return
        
        i = left - 1
        j = right + 1
        p = nums[(right + left) // 2]
        while i < j:
            i += 1
            j -= 1
            
            while nums[i] < p:
                i += 1
            
            while nums[j] > p:
                j -= 1
            
            if (i < j):
                nums[i], nums[j] = nums[j], nums[i]
        
        self.recurSort(nums, left, j)
        self.recurSort(nums, j + 1, right)