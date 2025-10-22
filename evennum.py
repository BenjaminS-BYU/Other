def find_nums(nums):
    total = []
    for i in nums:
        count = 0
        for j in str(i):
            count += 1
        if count % 2 == 0:
            total.append(count)
    return len(total)

print(find_nums([12,345,2,6,7896]))
print(find_nums([555,901,482,1771]))

