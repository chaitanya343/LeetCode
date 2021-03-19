def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]

def twoSum_withDict(nums, target):
    dic = {}
    for i, n in enumerate(nums): 
        if n in dic:
            return [dic[n], i]
        dic[target-n] = i

print(twoSum_withDict([2,8,11,15,7], 9))