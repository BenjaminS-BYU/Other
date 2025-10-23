arr = [1,0,2,3,0,4,5,0]
def duplicateZeros(arr):
    temp_arr = []
    for i in arr:
        if len(temp_arr) < len(arr):
            if i == 0:
                temp_arr.append(i)
            temp_arr.append(i)
    arr[:] = temp_arr[:len(arr)]



duplicateZeros(arr)
print(arr)
