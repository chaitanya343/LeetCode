def twoSumLessThanK(nums, k):
    maxSum = -1
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum < k and sum > maxSum:
                maxSum = sum
    return maxSum

def twoSumLessThanK_optimal(nums, k):
    nums.sort()
    lo, hi = 0, len(nums)-1
    ans = -1
    while lo < hi: 
        x = nums[lo] + nums[hi]
        if x < k: 
            lo += 1
            ans = max(ans, x)
        else: 
            hi -= 1
    return ans

print(twoSumLessThanK([34,23,1,24,75,33,54,8], 60))