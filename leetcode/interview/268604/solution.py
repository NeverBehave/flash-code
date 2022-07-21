def getSubsetNum(ls, k):
    res = 0
    if len(ls) == 0:
        return res

    s = sorted(ls)
    left, right = 0, len(ls) - 1

    # Multiple
    while left <= right:
        numleft = s[left]
        numright = s[right]

        if numleft + numright <= k:
            res += pow(2, right - left)
            
            left += 1
        else:
            right -= 1
                

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