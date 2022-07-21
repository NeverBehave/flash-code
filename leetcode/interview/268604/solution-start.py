def getSubsetNum(ls, k):
    res = 0
    if len(ls) == 0:
        return res

    s = sorted(ls)
    left, right = 0, 0
    
    while left < len(ls) and left <= right:
        numleft = s[left]
        numright = s[right]

        sk = numleft + numright
        if left == right:
            sk = numleft

        if sk <= k:
            inside = right - left - 1
            if inside > -1:
                res += pow(2, inside)
            else:
                res += 1
            
            if right == len(ls) - 1:
                left += 1
            else:
                right += 1
        else:
            left += 1
                

    return res

nums = [2, 4, 5, 7]
k = 8
o = 5
res = getSubsetNum(nums, k)
print(res, res == o)

nums = [1, 4, 3, 2]
k = 8
o = 15
res = getSubsetNum(nums, k)
print(res, res == o)

nums = [2, 4, 2, 5, 7]
k = 10
o = 27
res = getSubsetNum(nums, k)
print(res, res == o)