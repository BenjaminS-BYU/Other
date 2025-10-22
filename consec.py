def findMaxConsecutiveOnes(nums):
    running_total = 0
    count_list = []
    for i in nums:
        temp_list = []
        if i == 1:
            temp_list.append(i)
        if i in temp_list:
            running_total += 1
            count_list.append(running_total)
        else:
            count_list.append(running_total)
            running_total = 0
            temp_list.clear()
                        
    return max(count_list)

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))