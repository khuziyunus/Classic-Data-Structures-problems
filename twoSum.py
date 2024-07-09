def sum(nums,target):
    nums_dict = {}
    for i,num in enumerate(nums):
        compliment = target - num

        if compliment in nums_dict:
            return [nums_dict[compliment], i]      
          
        nums_dict[num] = i

    return[]
        

nums = [1, 2, 3, 4, 5, 6, 6, 7]
target = 10
print(sum(nums, target))  