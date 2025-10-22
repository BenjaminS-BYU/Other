def sorted_squares(nums):
    sqr_nums = []
    for i in nums:
        i **= 2
        sqr_nums.append(i)
    return sorted(sqr_nums)


print(sorted_squares([-4,-1,0,3,10]))
print(sorted_squares([-7,-3,2,3,11]))