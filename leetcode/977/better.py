class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        i, j = l - 1, -1
        res = []
        
        for i in range(l):
            if nums[i] >= 0:
                j = i
                break
        
        if j != -1:
            bk = j
            i = j - 1
            while i >= 0 and j < l:
                if abs(nums[i]) < abs(nums[j]):
                    res.append(pow(nums[i], 2))
                    i -= 1
                else:
                    res.append(pow(nums[j], 2))
                    j += 1
        
        
        if i >= 0:
            for x in range(i, -1, -1):
                res.append(pow(nums[x], 2))
        else:
            for x in range(j, l):
                res.append(pow(nums[x], 2))
            
        
        return res